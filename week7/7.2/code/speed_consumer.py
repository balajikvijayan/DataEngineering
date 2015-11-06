import time, json, ast, pyspark

from pprint import pprint
from kafka.client   import KafkaClient
from kafka.consumer import KafkaConsumer
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

KAFKA_TOPIC = 'mygram'
checkpointDir = r"C:\Anaconda\Galvanize\DataEngineering\week7\7.2\stream"
n=10
data = []

def buildContext():
	ssc = StreamingContext(SparkContext(), 1)
	ssc.checkpoint(checkpointDir)
	return ssc

def updateFunction(newValues, runningCount):
    if runningCount is None:
       runningCount = 0
    return sum(newValues, runningCount)

def partitionCount(datum):
    datatype = datum['dataunit'].keys()[0]
    if datatype.endswith('property'):
        return ('\\'.join((datatype,
            datum['dataunit'][datatype]['property'].keys()[0])), 1)
    else:
        return (datatype, 1)
	
if __name__ == "__main__":
	ssc = StreamingContext.getOrCreate(checkpointDir, buildContext)

	zkQuorum = "localhost:2181"
	kvs = KafkaUtils.createStream(ssc, zkQuorum, "spark-streaming-consumer", {KAFKA_TOPIC: 1})
	#data stream of data dictionaries
	ds = kvs.map(lambda data: ast.literal_eval(data[1]))

	ds.pprint()
	pprint(type(ds))
	# print type(ds)
	
	data.append(ds)
	if len(data) > 0 and len(data) % (n*13) == 0:
		path = "..\\speed\\"
		name = "speed" + str(len(data)/n*13) + ".json"
		with open (path+name, 'w') as outfile:
			for vals in data:
				json.dump(vals, outfile)
				outfile.write("\n")
		pprint(name + " written.")
	
	ssc.start()
	ssc.awaitTermination()
	
	# sumstats = ds.map(partitionCount).updateStateByKey(partitionCount)
	# ssc.stop(stopGraceFully=True) 