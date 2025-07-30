# 2025-07-29
# https://www.psc.edu/resources/training/hpc-workshop-big-data-july-29-30-2025/
import re
from pyspark import SparkConf, SparkContext
import sys

def main(filename):
	# Set up Spark context
	conf = SparkConf().setAppName("ShakespeareWordCount")
	sc = SparkContext(conf=conf)
	
	# Open a file
	if (len(filename) == 0):
		rdd = sc.textFile("Complete_Shakespeare.txt")
	else: 
		rdd = sc.textFile(filename)
	rdd.count()
	
	# wordsRDD = rdd.flatMap(lambda line: line.split())
	# to get better count, remove punctuation and convert everything to lowercase:
	wordsRDD = rdd.flatMap(lambda line: re.findall(r'\b\w+\b', line.lower()))
	wordCount = wordsRDD.count() 
	print(f"Word count: {wordCount}")
	distinctWords = wordsRDD.distinct()
	print(f"Distinct word count: {distinctWords.count()}")
	
	# Map each word to a (word, 1) pair
	wordPairsRDD = wordsRDD.map(lambda word: (word, 1))
	
	# Reduce by key (i.e., word) to count occurrences
	wordCountsRDD = wordPairsRDD.reduceByKey(lambda a, b: a + b)
	
	# Collect or sort as needed
	for word, count in wordCountsRDD.take(10):  # show sample output
	 	print(f"{word}: {count}")

	sc.stop()

if __name__ == "__main__":
	main("")