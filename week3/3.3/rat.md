Miniquiz
--------

1. What does *RDD* stand for?

2. Is `count()` a transformation or an action.

3. In `sc.parallelize(xrange(10)).filter(lambda x:x%2==0).collect()`
   where does `lambda` execute? On the driver or the executors? Also,
   where does `xrange(10)` execute?

4. In `sc.parallelize(xrange(10)).filter(lambda x:x == 0)` where does
   `lambda` execute? On the driver or the executors?

5. Write a Spark job that squares all numbers from 0 to 99.

6. If I read a file that is 100 MB from S3: What is the default
   partition size? How many partitions will hold this file?

7. Bonus: How does `.top()` work?