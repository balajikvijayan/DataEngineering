object CSVReader extends App {
    println("Date, Open, High, Low, Close, Volume, AdjClose")
    val bufferedSource = io.Source.fromFile("/data/appl.csv")
    for (line <- bufferedSource.getLines) {
        val cols = line.split(",").map(_.trim)
        // do whatever you want with the columns here
        println(s"line")
    }
    bufferedSource.close
}