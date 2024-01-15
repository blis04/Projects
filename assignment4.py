import hash
import change_word
import re
infile = open('gettysburg.txt','r')

allwordHash = hash.hash_table(600073)
commonHash = hash.hash_table(10039)

def wordVariation(word):
    # Create a list for words that are in hash's
    # create a list for each returned list to go into to check possibilities
    possibilityList = []
    shorterList = change_word.generate_one_letter_shorter(word)
    extraList = change_word.generate_one_letter_extra(word)
    swapLetterList = change_word.swap_one_letter(word)
    azList = change_word.swap_letter_az(word)
    splitList = change_word.split(word)

    # This will check each variation of function 1 in lab 12
    for variation in shorterList:
        if commonHash.search(variation) == True or commonHash.search(variation.lower()) == True:
            if variation not in possibilityList:
                possibilityList.append((variation))
        elif allwordHash.search(variation) == True or allwordHash.search(variation.lower()) == True:
            if variation not in possibilityList:
                possibilityList.append((variation))

    # This will check each variation of function 2 in lab 12
    for variation in extraList:
        if commonHash.search(variation) == True or commonHash.search(variation.lower()) == True:
            if variation not in possibilityList:
                possibilityList.append((variation))
        elif allwordHash.search(variation) == True or allwordHash.search(variation.lower()) == True:
            if variation not in possibilityList:
                possibilityList.append((variation))
    # This will check each variation of function 3 in lab 12
    for variation in swapLetterList:
        if commonHash.search(variation) == True or commonHash.search(variation.lower()) == True:
            if variation not in possibilityList:
                possibilityList.append((variation))
        elif allwordHash.search(variation) == True or allwordHash.search(variation.lower()) == True:
            if variation not in possibilityList:
                possibilityList.append((variation))
    # This will check each variation of function 4 in lab 12
    for variation in azList:
        if commonHash.search(variation) == True or commonHash.search(variation.lower()) == True:
            if variation not in possibilityList:
                possibilityList.append((variation))
        elif allwordHash.search(variation) == True or allwordHash.search(variation.lower()) == True:
            if variation not in possibilityList:
                possibilityList.append((variation))
    # This will check each variation of function 5 in lab 12
    for variation in splitList:
        if commonHash.search(variation) == True or commonHash.search(variation.lower()) == True:
            if variation not in possibilityList:
                possibilityList.append(variation)
        elif allwordHash.search(variation) == True or allwordHash.search(variation.lower()) == True:
            if variation not in possibilityList:
                possibilityList.append((variation))

    return possibilityList

with open('words.txt', 'r') as file:
    for eachLine in file:
        line = eachLine.strip()
        allwordHash.add(line)
# created hashtable 1 with all the words


with open('mostCommon5001.txt','r') as file:
    for eachLine2 in file:
        line2 = eachLine2.strip()
        commonHash.add(line2)
# created hashtable 2 with all the common words


wordlists = []
with open('gettysburg.txt', 'r') as file:
    lineNumber = 0
    for line in file:
        lineNumber += 1
        line = line.strip()
        list_of_words = re.split('\s|\.|,|\-|\?|!|;|\$|\*|\(|\)', line)
        # do all the stuff about checking spelling etc on each word in list_of_words
        # we now have a list of words from the document
        # we're gonna run it through my algorithms in lab 12 to find possible corrections
        for word in list_of_words:
            if word != '':
                if allwordHash.search(word) == False and allwordHash.search(word.lower()) == False:
                    # first check to make sure that it's not an uppercase issue
                    print(f'Line number: {lineNumber}')
                    print(line)
                    print(f'{word} is spelled incorrectly, possible correct spellings are: ')
                    possibilitylist = wordVariation(word)
                    for word in possibilitylist:
                        print(word)
                    print('\n')

