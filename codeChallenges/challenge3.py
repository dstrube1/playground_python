#challenge3
#https://www.linkedin.com/learning/python-code-challenges/sort-a-string

#Sort words in a sentence alphabetically

def sortWords(input):
	words = input.split(" ")
	words = sorted(words, key=lambda s: s.lower())
	output = ""
	for word in words:
		output += word + ' '
	return output

#instructor's solution (I like mine better)
def sort_words(input):
	words = input.split()
	words = [w.lower() + w for w in words]
	words.sort()
	words = [w[len(w)//2:] for w in words]
	return ' '.join(words)

input = "The quick brown fox jumped over the lazy dog."
print("sentence before: \n" + input)
output = sortWords(input)
print("sentence after: \n" + output)
print("sentence after: \n" + sort_words(input))