##Individual Assignment
###Objectives:
- Contrasting different file formats
- Understanding Partitioning
- Understanding Bucketing
- Understanding Skewed tables.

###Lab:

####File Formats
This lab assumes you have hive and its dependancies installed and running.   

- Step1: Download 100m movies data from `<Galvanize link>`
- Step2: Load data into hdfs
- Create `<tablename>_txt` to load data as text file.
- Create `<tablename>_rc` to load data in rc format.
- Create `<tablename>_orc` to load data in orc format.
- Step3: Load the data into above tables from hdfs and note the timings. Which table took more time to load?

- Step4: How many movies with the tag `Action` are present in the list? Save a list of the titles and IDs of such movie to the HDFS. Contrast the timings. *Hint : Case sensitive?*

####Partitioning
- Step1: Review the data in `hive2_<<country>>.txt`  
- Step2: Load the files to hdfs.  
- Step3: Create table `states` in hive with partition as `country`.  
- Step4: Query about the description of the table. 
- Step5: Load states with data from different files in hdfs.  
- Step6: Check the directory structure in HDFS. Which folder(s) should we be looking at?

####Bucketing
- Step1: Review data in movies.csv  
- Step2: Create table `movies1` **without** bucketing.    
- Step3: Create table `movies2` **with bucketing over movieID (4 buckets)**.  
- Step4: Load same data to both tables and notice difference in time.   
- Step5: Run count(*) command on both tables and notice difference in time.   
- Step6: Perform sampling on movies2

