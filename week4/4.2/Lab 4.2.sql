DROP TABLE IF EXISTS movies;

CREATE EXTERNAL TABLE movies(
  movieId INT,
  title STRING,
  genres STRING
)
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ","
STORED AS TEXTFILE
LOCATION "/user/root/movies/"
TBLPROPERTIES("skip.header.line.count"="1");

select * from movies;

DROP TABLE IF EXISTS ratings;

CREATE EXTERNAL TABLE ratings(
  userId INT,
  movieId INT,
  rating FLOAT,
  reviewtime BIGINT
)
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION '/user/root/ratings/'
TBLPROPERTIES("skip.header.line.count"="1");

select * from ratings;

DROP TABLE IF EXISTS links;

CREATE EXTERNAL TABLE links(
  movieId INT,
  imdbId INT,
  tmdbId INT
)
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION '/user/root/links/'
TBLPROPERTIES("skip.header.line.count"="1");

select * from links;

DROP TABLE IF EXISTS tags;

CREATE EXTERNAL TABLE tags(
  userId INT,
  movieId INT,
  tag STRING,
  tagtime BIGINT
)
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION '/user/root/tags/'
TBLPROPERTIES("skip.header.line.count"="1");

select * from tags;

select count(*) from movies;
select tag, count(*) from tags group by tag;