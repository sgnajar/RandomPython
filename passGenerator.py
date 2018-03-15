#   Author: Sasan Najar
#   Email: sasangnajar@gmail.com

#   This code is designed to have a function called getRandomPass that selects two random words from a list of words
##  STEP 1: Take a filename as input (in this case: words.txt)
##  STEP 2: Create a list of words
##  STEP 3: Return a string consisting of two random words concatenated together without spaces

import random

wordFile = "words.txt"
wordList = []

with open(wordFile,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			wordList.append(word)

def getRandomPass():
    return str().join(random.sample(wordList,2)) #if you want other than two words in your random pass generator you can simply change this number