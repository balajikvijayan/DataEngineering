import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._
import org.apache.spark.SparkConf
import org.apache.spark.rdd.RDD
import scala.io.Source

object SimpleApp {
  def main(args: Array[String]) {
    val logFile = "C:\\Anaconda\\Galvanize\\DataEngineering\\week3\\3.3\\data\\appl.csv"
    val conf = new SparkConf().setAppName("Simple Application").setMaster("local[4]").set("spark.executor.memory","1g")
    val sc = new SparkContext(conf)
    val logData = sc.textFile(logFile)
    val header = logData.first
    val data = logData.filter(_(0) != header(0))
    
//    val adjclose: RDD[Double] = data.map ( line => line.split(",").last.toDouble).cache()
//    val count = adjclose.count
//    val mean = adjclose.sum / count
//    val min = adjclose.min()
//    val max = adjclose.max()
//    val devs = adjclose.map(score => (score - mean) * (score - mean))
//    val stddev = Math.sqrt(devs.sum / count)
//    val dateadjclose: RDD[(String, Double)] = data.map ( line => (line.split(",")(0),line.split(",").last.toDouble)).cache()
//    val topdateadjclose = dateadjclose.sortBy(_._2, false)
//    val bottomdateadjclose = dateadjclose.sortBy(_._2, true)
//    val comparedate: RDD[(Double, Double)]  = data.map ( line => (line.split(",")(1).toDouble,line.split(",")(4).toDouble))
//    val datehigh = comparedate.filter({case (key, value) => value > key})
//    val datelow = comparedate.filter({case (key, value) => key  > value})
//    val datesame = comparedate.filter({case (key, value) => key  == value})
//    println("Count : %s".format(count))
//    println("Mean : %s".format(mean))
//    println("Min : %s".format(min))
//    println("Max : %s".format(max))
//    println("Var : %s".format(Math.pow(stddev, 2)))
//    println("Std Dev : %s".format(stddev))
//    println("Top Adj Close : %s, %s, %s".format(topdateadjclose.take(3)(0),topdateadjclose.take(3)(1),topdateadjclose.take(3)(2)))
//    println("Bottom Adj Close : %s, %s, %s".format(bottomdateadjclose.take(3)(0),bottomdateadjclose.take(3)(1),bottomdateadjclose.take(3)(2)))
//    println("Count of Stock Rise: %s".format(datehigh.count))
//    println("Count of Stock Fall: %s".format(datelow.count))
//    println("Count of Stock Same: %s".format(datesame.count))
//    println("Top 3 Log Most: %s".format(diff.first()))
    val stocklog : RDD[(String, (Double, Double))]  = data.map(line => (line.split(",")(0).toString,(math.log(line.split(",")(1).toDouble),math.log(line.split(",")(4).toDouble))))
    val diff : RDD[(String, Double)] = stocklog.map({case(key, (val1, val2)) => (key, (val1 - val2).toDouble)}).cache()
    val topdiff = diff.sortBy(_._2, false)
    val bottomdiff = diff.sortBy(_._2, true)
    println("Top 3 Log Change: %s, %s, %s".format(topdiff.take(3)(0),topdiff.take(3)(1),topdiff.take(3)(2)))
    println("Bottom 3 Log Change : %s, %s, %s".format(bottomdiff.take(3)(0),bottomdiff.take(3)(1),bottomdiff.take(3)(2)))
    }
}