#word = str(input("Enter the word you would like to use: "))
#word = word.lower()

def generate_one_letter_shorter(word):
    results1 = []

    for i in range(len(word)):
        shorter_word = word[:i] + word[i + 1:]
        results1.append(shorter_word)

    return results1


def generate_one_letter_extra(word):
    results2 = []

    for i in range(len(word)+1):
        for az in range(26):
            extraLetter = word[:i]+chr(97+az)+word[i:]
            results2.append(extraLetter)

    return results2

def swap_one_letter(word):
    results3 = []
    for i in range(len(word) - 1):
        swapped_word = word[:i] + word[i + 1] + word[i] + word[i + 2:]
        results3.append(swapped_word)

    return results3

def swap_letter_az(word):
    result4 = []

    for i in range(len(word)+1):
        for az in range(26):
            extraLetter = word[:i]+chr(97+az)+word[i+1:]
            result4.append(extraLetter)

    return result4

def split(word):
    result5 = []

    for i in range(1,len(word)):
        split = word[:i]
        rest = word[i:]
        result5.append(split + rest)

    return result5

with open('config.txt','r') as file:
    for eachLine in file:
        line = eachLine.strip()

def read_allwords():
    with open('words.txt', 'r') as file:
        for eachLine in file:
            line = eachLine.strip()

def read_commonwords():
    with open('mostCommon5001.txt','r') as file:
        for eachLine in file:
            line = eachLine.strip()



