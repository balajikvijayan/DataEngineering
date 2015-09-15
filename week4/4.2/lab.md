## Step 1: Start Hive

Follow the steps in the lecture to start your Hortonworks Sandbox VM.

Start 2 `ssh` session2 into it.

Start the Hive shell in one session.

Leave the other session running the Bash shell. 


## Step 2: Upload Movielens Data to HDFS

Download the MovieLens data files from the web (`ml-latest-small`).

Unzip it and upload these files into HDFS:

- `links.csv`
- `movies.csv`
- `ratings.csv`
- `tags.csv`

## Step 3: Create Tables

Here are the header lines from the files.

File           |First Line
----           |----------
`links.csv `   |`movieId,imdbId,tmdbId`
`movies.csv`   |`movieId,title,genres`
`ratings.csv`  |`userId,movieId,rating,timestamp`
`tags.csv `    |`userId,movieId,tag,timestamp`

Execute `CREATE TABLE` commands to create internal tables for each of
these files.

Use `DESCRIBE FORMATTED` to verify that the tables are created
correctly.

## Step 4: Hive Queries

Write Hive Queries to perform the following actions.

- Count the number of movies in the `movies` table.

- Count the number of distinct tags grouped by tags.

## Step 5: Extra Challenge

- For each movie find how many ratings it has.

- For each movie find out the average rating.

- Find top 10 movies with the highest average ratings that have at least 5 ratings.

## Step 6: Drop Tables

- When you are done drop the tables.

- Do you need to do anything else to get rid of the data?
