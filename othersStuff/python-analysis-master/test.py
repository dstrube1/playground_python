# Import the tools we will be using

def returningBeforeImporting():
	print("returning before importing")
	return True#False#

def setup():
	#these each fail from just python, during python_analysis class; must try after
	import numpy as np
	import matplotlib.pyplot as plt
	import pandas as pd
	import seaborn as sns
	from scipy import stats

#test.py
# Load in some data
def main():
	if returningBeforeImporting():
		return
	else:
		setup()
	tips_ds = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")
	# This loads in our data as a DataFrame object, labeled columns and rows
	# A DataFrame is a 2D mutable data structure, so we can view it as a table
	print(type(tips_ds))
	print(tips_ds)
	
main()
#from /Users/dstrube/Downloads/python-analysis-master
#jupyter notebook