
# returns the entirety of "Dracula" as a string
def readBook():
  f = open("dracula.txt", "r")
  s = f.read().replace("-", " ")
  f.close()
  return ''.join(c for c in s if c.isalnum() or c == " ")

# read file
dracula = readBook()

# Everything till now is provided: the main purpose is to inport the story folder function will read the book, and return the entire text of it as a string, ready to be stored in a variable. Then, Simply create a variable to hold the story of Dracula, and then assign it to the result of this function, as in line 9.



# split text by word / convert words to lowercase. [It iterates through each word in the list obtained from dracula.split() and converts each word to lowercase using the .lower() method. The result is a new list with all the words in lowercase.]


words = [words.lower() for words in dracula.split()]



# stylize header [\n prints a new line]
header = "Dracula \n -- Text Analytics --"
print(f"{header}\n")

# most common word
# initialize variables
mostCommonWord = ""
maxCount = 0

# store word with count count
wordCount = {}

# iterate over words
for word in words: # for loop will iterate through the story splitted words

  # count occurances
  if word in wordCount:
# will check if the word is already in the created dictionary

    wordCount[word] += 1 
# if yes it will add 1 for the sword count of just this word

  else:
    wordCount[word] = 1 
# otherwise it will add this word to the dictionary and start the word count for this number by 1

  # iterate through word count
  if wordCount[word] > maxCount: 
# if the word count of that word is greater than mac count, the replace max count with the bigger value which is the count of that word.

    maxCount = wordCount[word]
    mostCommonWord = word 
# most common repeated word

print(f"The most common word is '{mostCommonWord}' appearing {maxCount} times\n")

# how many unique four-letter words are in the book
# initialize list
fourLetterWords = []

# iterate over text
for word in words:
  # if length word is 4 and not in list [This code will help you count the occurrences of unique four-letter words in the lowercase "Dracula" text while ignoring duplicates.]


  if (len(word) == 4 and word not in fourLetterWords):
    fourLetterWords.append(word)
    
print(f"There are {len(fourLetterWords)} unique 4 letter words\n")

# every word that shows up more than 500 times
# initialize list
wordsOver500 = []

# iterate over dict and save to new list
for word in wordCount:
  if wordCount[word] > 500:
    wordsOver500.append(word)

# print word and counts
for word in wordsOver500:
  print(f"{word}: {wordCount[word]} times")

