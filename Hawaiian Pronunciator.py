# Author:  Surmud Jamil
# Description: Gives the pronunciation of Hawaiian words


# info for getting choice
ANSWERS  = ["y", "yes", "n", "no"]
CONTINUE = "Do you want to enter another word? (y/yes/n/no): "


# info about characters
HYPHEN      = "-"
OKINA       = "'"
VOWELS      = ["a", "e", "i", "o", "u"]
VOWEL_SOUND = ["-AH-", "-EH-", "-EE-", "-OH-", "-OO-"]
COMP_VOWELS = ["ai", "ae", "ao", "au", "ei", "eu", "iu", "oi", "ou", "ui"]
COMP_SOUND = ["-EYE-", "-EYE-", "-OW-", "-OW-", "-AY-", "-EH-OO-", "-EW-",\
				 "-OY-", "-OW-","-OOEY-"]

VALID_CHARACTERS = ["h", "k", "l", "m", "n", "p", "w", "'", "a", "e", "i", \
					 "o", "u", " "]
W_VOWELS = ["a", "e", "i"] #vowels that turn w to v, if placed before



###################################################
# getChoice() prompts and reprompts the user until
#             they select a valid choice
# Parameters: question; a string to be asked
#             options; a list of string options
# Return:     choice; a string chosen by the user
def getChoice(question, options):
	i = 0
	while i < len(options):
		print(options[i], end = "/")
		i = i + 1
	print()
	answer = input(question)
	while answer not in question:
		print("Please select a valid choice: ")
		answer = input(question)

	return answer

# def getHawaiianPhrase()
# Asks the user to input a Hawaiian phrase, re-prompting them if
# the phrase is not valid 
# parameters: Function takes in no input
# Return: Returns a string of the user’s chosen Hawaiian phrase
def getHawaiianPhrase():
	phrase = input("Enter a Hawaiian phrase to pronounce: ")
	invalidPhrase = True
	wordsInPhrase = []
	
	
	#cycle through the phrase and check if each character is valid
	count = 0
	while invalidPhrase == True:
		validCharacter = True
		validVowel = True
		wordsInPhrase = phrase.split()

		while count < len(phrase):
                #loop makes sure there's no invalid letters
                        
			if phrase[count].lower() not in VALID_CHARACTERS:
				print("The letter", phrase[count], "is not valid.")
				validCharacter = False

			count = count + 1	

		count = 0
		while count < len(wordsInPhrase):
                #loop makes sure word ends in a vowel
			if wordsInPhrase[count][len(wordsInPhrase[count])-1] not in VOWELS:
				print("The word", wordsInPhrase[count],\
				 		"does not end in a vowel.")	
				validVowel = False
			count = count + 1

		else:
			validVowel = True

		if validCharacter == True and validVowel == True: 
			invalidPhrase = False
			return phrase
			
			
		if invalidPhrase == True:
			phrase = input("Enter a Hawaiian phrase to pronounce: ")

	
		
#def pronounceW(word, index)
# Determines how a “w” should be pronounced
# Takes in a string and an integer
# The string is the word the “w” exists in
# The integer is the index where the “w” resides
# Returns a single character string
# pronounced as a v when there's an a, e, or i before it
def pronounceW(word, index):
	#for the w to be replaced with a v:
	#  - index must be at least 1
	#  - index must be equal to w
	#  - letter before index has to be a special letter
	if index > 0 and word[index] == "w" and word[index - 1] in W_VOWELS:
		return "v"
	else:
		return "w"

#def simpleVowel(letter)
# Determines how a vowel is pronounced
# Takes in a single-character string
# Returns a string, how the vowel is pronounced
def simpleVowel(letter):
	#assign the correct vowel sound to each vowel and return the sound
	letter = letter.lower()
	if letter == VOWELS[0]:
		return VOWEL_SOUND[0]

	elif letter == VOWELS[1]:
		return VOWEL_SOUND[1]

	elif letter == VOWELS[2]:
		return VOWEL_SOUND[2]

	elif letter == VOWELS[3]:
		return VOWEL_SOUND[3]

	elif letter == VOWELS[4]:
		return VOWEL_SOUND[4]


#def complexVowel(vowels)
# Determines how a complex, two-letter vowel is pronounced
# Takes in a two-character string
# Returns a string, how the complex vowel is pronounced
def complexVowel(vowel):
	vowel = vowel.lower()
	#assign the correct vowel sound to each vowel and return the sound
	if vowel == COMP_VOWELS[0]:
		return COMP_SOUND[0]

	elif vowel == COMP_VOWELS[1]:
		return COMP_SOUND[1]

	elif vowel == COMP_VOWELS[2]:
		return COMP_SOUND[2]

	elif vowel == COMP_VOWELS[3]:
		return COMP_SOUND[3]

	elif vowel == COMP_VOWELS[4]:
		return COMP_SOUND[4]

	elif vowel == COMP_VOWELS[5]:
		return COMP_SOUND[5]

	elif vowel == COMP_VOWELS[6]:
		COMP_SOUND[6]

	elif vowel == COMP_VOWELS[7]:
		COMP_SOUND[7]

	elif vowel == COMP_VOWELS[8]:
		COMP_SOUND[8]

	elif vowel == COMP_VOWELS[9]:
		COMP_SOUND[9]

	elif vowel == COMP_VOWELS[10]:
		COMP_SOUND[10]



# def pronounce(phrase)
# Determines how to pronounce an entire phrase
# Takes a string, possibly with multiple words
# Returns a string containing the complete phrase’s pronunciation
def pronounce(phrase):
	wordList = phrase.split(" ")
	count = 0
	while count < len(wordList):
		word = wordList[count]
		wordList[count] = pronounceWord(word)
		count = count + 1

	phrase = " ".join(wordList)
	phrase = phrase.upper()
	return phrase


# def pronounceWord(word)
# Determines how to pronounce a single word
# Takes in a string (with no spaces)
# Returns a string containing the word’s pronunciation
def pronounceWord(word):
	word = word.lower()
	# - break the function up into seperate loops 
	#       simple vowels
	#       complex vowels
	#       w's
	
	#while loop to check for a 'w'
	i = 0
	while i < len(word): 
		letter = word[i]
		if letter == "w":

	#If the letter at the index is w, and the output of pronounceW is a 
	#V, replace the w with a v 
			if pronounceW(word, i) == "v": 
				word = word[0:i] + "v" + word[i+1:len(word)]

		i = i + 1

	#while loop to check for complex vowels
	startCount = 0
	endCount = 2
	while endCount <= len(word): 

		wordSegment = word[startCount: endCount]
		if wordSegment in COMP_VOWELS:
			word = word[0:startCount] + complexVowel(wordSegment)+\
			word[endCount:len(word)]

		startCount = startCount + 1
		endCount = endCount + 1

	#while loop to check and replace normal vowels
	count = 0
	while count < len(word): 
		letter = word[count]
		if letter in VOWELS:
			word = word[0:count] + simpleVowel(letter) +\
                                word[count+1:len(word)]
		count = count + 1

	return word



def main():
	phrase = getHawaiianPhrase()
	pronnouncedPhrase = pronounce(phrase)
	print("The phrase", phrase, "is pronounced", pronounce(phrase))

	userResponse = getChoice(CONTINUE, ANSWERS)
	while userResponse != "n" and userResponse != "no":

		phrase = getHawaiianPhrase()
		pronnouncedPhrase = pronounce(phrase)
		print("The phrase", phrase, "is pronounced", pronounce(phrase))

		userResponse = getChoice(CONTINUE, ANSWERS)

	print("Thank you for using my Hawaiian Translator")

main()

