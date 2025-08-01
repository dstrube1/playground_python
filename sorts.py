# various sorts, starting with bubble sort from here:
# https://www.linkedin.com/learning/programming-foundations-algorithms-22973142/the-bubble-sort?autoSkip=true&resume=false&u=0

def bubbleSort(dataset):
	#Poor performance: O(n^2)
	
	# start with the array length and decrement each time
	for i in range(len(dataset) - 1, 0, -1):
		#print("i: ", i)
		for j in range(i):
			#print("j: ", j)
			# Check to see if the value at the index is greater than its neighbor
			if dataset[j] > dataset[j+1]:
				# If so, swap them
				temp = dataset[j]
				dataset[j] = dataset[j+1]
				dataset[j+1] = temp
		#print("Current state: ", dataset)

def mergeSort(dataset):
	#Divide and conquer
	# O(n log n)
	if len(dataset) > 1:
		mid = len(dataset) // 2
		left = dataset[:mid]
		right = dataset[mid:]
		
		# Recursively break down the arrays
		mergeSort(left)
		mergeSort(right)
		
		# Perform merging
		i = 0 # index into the left array
		j = 0 # index into the right array
		k = 0 # index into the merged array
		
		# While both arrays have content
		while i < len(left) and j < len(right):
			# Check to see if the value at the left index is less than the value at the right index
			if left[i] < right[j]:
				dataset[k] = left[i]
				i += 1
			else:
				dataset[k] = right[j]
				j += 1
			# Either way, increment the merge array index
			k += 1
		
		# If the left array still has values, add them
		while i < len(left):
			dataset[k] = left[i]
			k +=1
			i += 1
		
		# If the right array still has values, add them
		while j < len(right):
			dataset[k] = right[j]
			k +=1
			j += 1

def quickSort(dataset, first, last):
	# Also divide and conquer, also O(n log n), also recursive, but generally better than mergeSort
	# Operates in place on the data - doesn't need extra memory to do its work
	# Tradeoff: worst case scenario: O(n^2) when data is mostly sorted already
	
	# Pivot point selection
	if first < last:
		# Calculate the split point:
		pivotIndex = partitionX(dataset, first, last)
		
		# Now sort the two partitions
		quickSort(dataset, first, pivotIndex-1)
		quickSort(dataset, pivotIndex+1, last)
	

def partitionX(dataset, first, last):
	# TODO: does naming this dataset mess things up? If so, name it something else like dataValues

	# Choose the first item as the pivot value
	pivotValue = dataset[first]
	
	# Establish the upper and lower indices
	lowerIndex = first +1
	upperIndex = last
	# Start searching for the crossing point
	done = False
	while not done:
		# Advance the lower index
		while lowerIndex <= upperIndex and dataset[lowerIndex] <= pivotValue:
			# Move lower to the right
			lowerIndex += 1
		# Advance the upper index
		while upperIndex >= lowerIndex and dataset[upperIndex] >= pivotValue:
			# Move upper to the left
			upperIndex -= 1
		
		# If the two indices cross, then we have found the split point
		if upperIndex < lowerIndex:
			done = True
		else:
			temp = dataset[lowerIndex]
			dataset[lowerIndex] = dataset[upperIndex]
			dataset[upperIndex] = temp

	# When the split point is found, exchange the pivot value
	temp = dataset[first]
	dataset[first] = dataset[upperIndex]
	dataset[upperIndex] = temp
	
	# Return the split point index
	return upperIndex

# TODO: automate random populating of this list
list0 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

print("bubbleSort: ")
list1 = list0.copy()
print("Start: ", list1)
bubbleSort(list1)
print("Result: ", list1)

# TODO: in order to make sure that there is no function cross contamination 
# (ie, reusing variable name dataset), use new list for each example
print("mergeSort: ")
list2 = list0.copy()
print("Start: ", list2)
mergeSort(list2)
print("Result: ", list2)

print("quickSort: ")
list3 = list0.copy()
print("Start: ", list3)
quickSort(list3, 0, len(list3)-1)
print("Result: ", list3)

