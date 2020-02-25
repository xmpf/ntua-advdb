#!/usr/bin/env python

'''
Import Libraries
'''
# python3 print
from __future__ import print_function

# exit syscall
from sys import exit
from time import asctime

try:
    import numpy as np
except ImportError:
    print("Unable to find numpy library.")
    exit(-1)

# spark libraries
try:
    from pyspark import SparkConf
    from pyspark import SparkContext
    from pyspark.sql import SparkSession
    from pyspark.mllib.clustering import KMeans
    from pyspark.mllib.clustering import KMeansModel
except ImportError:
    print("Unable to find Spark libraries.")
    exit(-1)

try:
    from haversine import haversine
except ImportError:
    print("Unable to load haversine module.\n" +\
          "Either install it by: pip install haversine --user\n" +\
          "or press Y to import a custom implementation")
    ans = input('Load custom implementation? ')
    if 'yY' not in ans[0]: exit(0)
    from local_haversine import haversine

'''
Constants
'''
# DEBUG
DEBUG=True

# Application Specific
MAX_ITERS=3
NO_CENTROIDS=5

# ================ SPARK Related ===================
MASTER_CON='spark://master:7077'
DATASET_TRIPS='hdfs://master:9000/yellow_tripdata_1m.csv'
OUT_DIR='hdfs://master:9000/output'
NO_TASKS=10
# ==================================================

# Terminal Colors to use while Debugging
DBG_BLUE="\033[34m"
DBG_RED="\033[91m"
DBG_YELLOW="\033[93m"
DBG_RST="\033[39m"

def closestPoint(point, centroids):
    '''
    Find a point from centroids that its distance is minimum to the given point
    '''
    midx  = 0
    mdist = float("+inf")
    for i in range(len(centroids)):
        dist = haversine(point, centroids[i])
        if mdist > dist:
            mdist = dist
            midx  = i
    return midx

def parseVector(line):
        return np.array([float(x) for x in line.split(",")[3:5]])

if __name__ == '__main__':

    # Spark Configuration
    if DEBUG: print("Creating SPARK session...")
    conf = SparkConf()\
           .setAppName('K-Means')\
           .setMaster(MASTER_CON)  

    # Spark Context
    sc = SparkContext(conf=conf)

    # read dataset
    if DEBUG: print("Fetching data from " + DATASET_TRIPS + "...")
    rdd = sc.textFile(DATASET_TRIPS, NO_TASKS)
    trips = rdd.map(lambda line: (parseVector(line)))\
            .filter(lambda x: x[0] and x[1])\
            .cache()
    
    # apply k-means algorithm
    if DEBUG: print("Running K-Means algorithm...")

    # initial centroids are the first five elements
    centroids = np.array(trips.take(5))
    # sc.parallelize(centroids)

    for i in range(MAX_ITERS):
        closest = trips.map(lambda x: (closestPoint(x, centroids), (x, 1)))
        ps = closest.reduceByKey(lambda x, y: ((x[0][0] + y[0][0], x[0][1] + y[0][1]), x[1] + y[1]))
        newPoints = ps.map(lambda (x, ((y, z), w)): (y / float(w), z / float(w)))\
                    .collect()
        centroids = np.array(newPoints)

    # output directory
    timestamp = asctime().split(' ')[3].replace(':', '')
    output = OUT_DIR + '/' + timestamp
    
    print("Saving into " + output + "...")
    sc.parallelize(centroids, 1)\
      .saveAsTextFile(output)

    # exit normally
    exit(0)