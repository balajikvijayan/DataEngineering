import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._
import org.apache.spark.SparkConf
import org.apache.spark.rdd.RDD
import scala.io.Source
import com.typesafe.config.ConfigFactory

object ThreeFourLab {
  def main(args: Array[String]) {
    val logFile = "C:\\Anaconda\\Galvanize\\DataEngineering\\week3\\3.4\\data\\toy_data.txt"
//     val conf = new SparkConf().setAppName("3.4 Lab").setMaster("local[4]").set("spark.executor.memory","1g")
    val sc = new SparkContext("spark://127.0.0.1:7077",
                              "3.4 Lab", 
                              "C:\\spark-1.4.1-bin-hadoop2.4", 
                              List("C:\\Anaconda\\Galvanize\\DataEngineering\\week3\\3.4\\.34Lab\\target\\scala-2.10\\34-lab_2.10-1.0.jar"))

    val data = sc.textFile(logFile)
//    data.collect().foreach(println)
    val jsondata: RDD[(String, Int)] = data.map(line => (line.split(":")(0).replace("{","").replace("\"","").replace(" ", ""),(line.split(":")(1).replace("}","").replace("\"","").replace(" ", "").toInt)))
    jsondata.filter({case (key, value) => value > 5}).collect().foreach(println)
    val maxdata = jsondata.aggregateByKey(Int.MinValue)(Math.max(_,_), Math.max(_,_)).collect
    val mindata = jsondata.aggregateByKey(Int.MaxValue)(Math.min(_,_), Math.min(_,_)).collect
    maxdata.foreach(println)
    mindata.foreach(println)
    println(jsondata.values.reduce((x1, x2) => x1+x2))
    sc.stop()
    }
}