from __future__ import print_function
import time, json, ast, pyspark, sys

from pprint import pprint
from kafka.client   import KafkaClient
from kafka.consumer import KafkaConsumer
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

KAFKA_TOPIC = "mygram"
checkpointDir = r"C:\Anaconda\Galvanize\DataEngineering\week7\7.2\stream"
n=10
data = []

def updateFunction(newValues, runningCount):
    if runningCount is None:
       runningCount = 0
    return sum(newValues, runningCount)

def partitionCount(datum):
    datatype = datum['dataunit'].keys()[0]
    if datatype.endswith('property'):
        return ('\\'.join((datatype,
            datum['dataunit'][datatype]['property'].keys()[0])), 1)
    # else:
        # return (datatype, 1)

def writeHbase(datum):
    if datum['dataunit']['person_property']['property']['website'] is not None:
        val = []
        personid = datum['dataunit']['person_property']['id']['person_id']
        website = datum['dataunit']['person_property']['property']['website']
        colf = "cf"
		colname = "website"
        ts = datum['pedigree']['true_as_of_secs']

        val.append(personid)
        val.append(col)
        val.append(website)
        val.append(ts)
        return (val[0], val[:4])
	# else:
		# return None

def sendRecord(rdd):
	host = "127.0.0.1"
	table = "person"
	conf = {"hbase.zookeeper.quorum": host,
		"hbase.mapred.outputtable": table,
		"mapreduce.outputformat.class": "org.apache.hadoop.hbase.mapreduce.TableOutputFormat",
		"mapreduce.job.output.key.class": "org.apache.hadoop.hbase.io.ImmutableBytesWritable",
		"mapreduce.job.output.value.class": "org.apache.hadoop.io.Writable"}
	keyConv = "org.apache.spark.examples.pythonconverters.StringToImmutableBytesWritableConverter"
	valueConv = "org.apache.spark.examples.pythonconverters.StringListToPutConverter"

	#execute send
	rdd.map(writeHbase).saveAsNewAPIHadoopDataset(
			conf=conf,
			keyConverter=keyConv,
			valueConverter=valueConv)	 
	
if __name__ == "__main__":

	sc = SparkContext(appName = "Hbase")
	ssc = StreamingContext(sc, 1)
	# ssc.checkpoint(checkpointDir)
	# ssc = StreamingContext.getOrCreate(checkpointDir, buildContext)

	zkQuorum = "localhost:2181"
	kvs = KafkaUtils.createStream(ssc, zkQuorum, "spark-streaming-consumer", {KAFKA_TOPIC: 1})
	#data stream of data dictionaries
	
	ds = kvs.map(lambda data: ast.literal_eval(data[1]))
	ds.pprint()
	if ds is not None:
		ds.foreachRDD(sendRecord)
	
	ssc.start()
	ssc.awaitTermination()
	
	# sumstats = ds.map(partitionCount).updateStateByKey(partitionCount)
	# ssc.stop(stopGraceFully=True) 