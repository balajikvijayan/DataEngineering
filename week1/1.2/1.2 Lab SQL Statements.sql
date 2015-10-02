CREATE TABLE IP (
    ip varchar(13) PRIMARY KEY);
	
CREATE TABLE Link (
    source varchar(30) NOT NULL,
	destination varchar(30) NOT NULL,
	trusted boolean,
	ts time,
	PRIMARY KEY (source, destination)
	);
	
CREATE TABLE Geolocation (
    ip_start varchar(40) NOT NULL
,   ip_end varchar(40) NOT NULL
,   country varchar(2)
,   stateprov VARCHAR(100)
,   city VARCHAR(100)
,	PRIMARY KEY (ip_start, ip_end)
);
	
CREATE TABLE TMP (
	source varchar(30),
	trusted boolean,
	datetimeval time,
	destinations varchar(40)[]
);

insert into Link select source, unnest(destinations), trusted, datetimeval from TMP;

alter table Link
add foreign key (source)
references IP(ip);

alter table Link
add foreign key (destination)
references IP(ip);

COPY Geolocation FROM 'C:\Anaconda\Galvanize\DataEngineering\week1\1.2\dbip-city-2015-07.csv' DELIMITER ',' CSV ENCODING 'UTF8';

COPY TMP FROM 'C:\Anaconda\Galvanize\DataEngineering\week1\1.2\link.log' FORMAT TEXT DELIMITER '\t' ENCODING 'UTF8';