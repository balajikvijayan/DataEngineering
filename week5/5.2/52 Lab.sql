DROP TABLE IF EXISTS movies_txt;

CREATE EXTERNAL TABLE movies_txt(
  movieId INT,
  title STRING,
  genres STRING
)
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ","
STORED AS TEXTFILE
LOCATION "/user/root/movies/"
TBLPROPERTIES("skip.header.line.count"="1");

select * from movies_txt;

DROP TABLE IF EXISTS movies_rc;

-- Create external table.
CREATE EXTERNAL TABLE movies_rc(
  movieId INT,
  title STRING,
  genres STRING
)
STORED AS ORC;

-- Insert data.
INSERT OVERWRITE TABLE movies_rc
SELECT * 
FROM movies_txt;

-- Select table to test.
SELECT * FROM movies_rc;

DROP TABLE IF EXISTS movies_avro;

-- Create external table.
CREATE EXTERNAL TABLE movies_avro(
  movieId INT,
  title STRING,
  genres STRING
)
STORED AS AVRO
LOCATION "/user/root/movies/avro/";

-- Insert data.
INSERT OVERWRITE TABLE movies_avro
SELECT * 
FROM movies_txt;

-- Select table to test.
SELECT * FROM movies_avro;

DROP TABLE IF EXISTS movies_avro;

-- Create external table.
CREATE EXTERNAL TABLE movies_avro_small(
  movieId INT,
  title STRING
)
STORED AS AVRO
LOCATION "/user/root/movies/avro/small";

-- Insert data.
INSERT OVERWRITE TABLE movies_avro_small
SELECT movieId, title FROM movies_avro WHERE genres like '%Action%';

-- Select table to test.
SELECT * FROM movies_avro_small;

hive -e "SELECT movieId, title FROM movies_avro WHERE genres like '%Action%'" > /user/root/movies/avro/movies_avro.csv

DROP TABLE IF EXISTS statepop;

CREATE EXTERNAL TABLE statepop(
  country string,
  statename string,
  population bigint
)
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ","
STORED AS TEXTFILE
LOCATION "/user/root/states";

select * from statepop;

DROP TABLE if exists statepop_part;

CREATE TABLE statepop_part(
  statename string,
  population bigint
)
PARTITIONED BY (country string)
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ","
STORED AS TEXTFILE
LOCATION "/user/root/states/parts";

FROM statepop
INSERT INTO TABLE statepop_part PARTITION(country)
SELECT statename, population, country;

select * from statepop_part;

DROP TABLE IF EXISTS movies_txt;

CREATE EXTERNAL TABLE movies1(
  movieId INT,
  title STRING,
  genres STRING
)
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ","
STORED AS TEXTFILE
LOCATION "/user/root/movies/"
TBLPROPERTIES("skip.header.line.count"="1");

select * from movies1;

SET hive.enforce.bucketing=true;
CREATE EXTERNAL TABLE movies2(
  movieId INT,
  title STRING,
  genres STRING
)
CLUSTERED BY (movieId) into 4 BUCKETS
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ","
STORED AS TEXTFILE
LOCATION "/user/root/movies/buckets";

FROM movies1
INSERT INTO TABLE movies2
select *;

select * from movies2;