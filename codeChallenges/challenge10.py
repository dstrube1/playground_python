#challenge10
#https://www.linkedin.com/learning/python-code-challenges/count-unique-words?u=2163426

#count the number of unique words and how often each occurs

#inut: path to a text file
#output: print total number of words, & top 20 most frequent words & number of occurrences for each

def countWords ( inputFile ) :
	words = {}
	with open(inputFile, 'rt') as fileIn:
		for lineF in fileIn:
			wordsInLine = lineF.split(' ')
			for word in wordsInLine:
				if word.isspace():
					continue
				word = word.lower()
				if word in words:
					words[word] += 1
				else:
					words[word] = 1
	count = 1
	print("total number of words: " + str(len(words)))
	print("top 20:")
	for word in sorted(words, key=words.get, reverse=True):
		print(str(count) + ": " + word + " = " + str(words[word]))
		count += 1
		if count > 20:
			break

#instructor's solution, pretty good:
import re
from collections import Counter
def count_words (inputFile):
	with open(inputFile, encoding="utf-8") as file:
		allWords = re.findall(r"[0-9a-zA-Z-']+", file.read())
		allWords = [word.upper() for word in allWords]
		print("Total words:", len(allWords))
		
		wordCounts = Counter()
		for word in allWords:
			wordCounts[word] += 1
		print("Top 20: ")
		for word in wordCounts.most_common(20):
			print(word[0], "\t", word[1])

#main
countWords ( "challenge10.py" )
count_words( "challenge10.py" )

#since this file is the input of the function, let's add a lot of text
#to make it a useful input:
"""
Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.
Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this.

But, in a larger sense, we can not dedicate — we can not consecrate — we can not hallow — this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us—that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion — that we here highly resolve that these dead shall not have died in vain — that this nation, under God, shall have a new birth of freedom — and that government of the people, by the people, for the people, shall not perish from the earth.

[Needs more text]

The Gettysburg Address is a speech that U.S. President Abraham Lincoln delivered during the American Civil War at the dedication of the Soldiers' National Cemetery in Gettysburg, Pennsylvania, on the afternoon of Thursday, November 19, 1863, four and a half months after the Union armies defeated those of the Confederacy at the Battle of Gettysburg. It is one of the best-known speeches in American history.[4][5]

Not even the day's primary speech, Lincoln's carefully crafted address came to be seen as one of the greatest and most influential statements of American national purpose. In just 271 words, beginning with the now iconic phrase "Four score and seven years ago,"‍ referring to the signing of the Declaration of Independence[6] 87 years earlier, Lincoln described the US as a nation "conceived in Liberty, and dedicated to the proposition that all men are created equal," and represented the Civil War as a test that would determine whether such a nation, the Union sundered by the secession crisis,[7] could endure. He extolled the sacrifices of those who died at Gettysburg in defense of those principles, and exhorted his listeners to resolve

that these dead shall not have died in vain—that this nation, under God, shall have a new birth of freedom[8]—and that government of the people, by the people, for the people, shall not perish from the earth.[6][9]
Despite the prominent place of the speech in the history and popular culture of the United States, its exact wording is disputed. The five known manuscripts of the Gettysburg Address in Lincoln's hand differ in a number of details, and also differ from contemporary newspaper reprints of the speech. Neither is it clear where stood the platform from which Lincoln delivered the address. Modern scholarship locates the speakers' platform 40 yards (or more) away from the traditional site in Soldiers' National Cemetery at the Soldiers' National Monument, such that it stood entirely within the private, adjacent Evergreen Cemetery.
"""
