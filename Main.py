'''
Written in Python 3 using Pycharm IDE
A simple program that looks over a text file
and outputs some interesting information about it.
Takes in one command line argument
'''

import sys
import os
import string
from collections import Counter

# Some Macros (sort of)
MOST = 0
LEAST = 1
NUMBER = 2
CHARACTERS = 3
LONGEST = 4
LINES = 5

def fill_data(file_path, list):

    data = Counter()
    with open(file_path) as f:
        for line in f:
            print("{}".format(line))

            # Make sure everything is lowercase and no punctuations to create separate entries
            transtable = str.maketrans(string.punctuation, ' '*len(string.punctuation))
            newline = line.rstrip('\n').translate(transtable).lower()
            words = newline.split()
            data.update(words)

            list[LINES] += 1
            list[CHARACTERS] += len(line)
            list[NUMBER] += len(words)

    items = data.most_common()
    list[MOST] = items[0][0]
    list[LEAST] = items[-1][0]
    list[LONGEST] = items[-1][0]

    for item in items:
        if len(item[0]) > len(list[LONGEST]):
            list[LONGEST] = item[0]

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("Error: Invalid arguments. python Main.py FILE_PATH")
        sys.exit()
    file_path = sys.argv[1]
    print("Chosen file is: {}".format(file_path))

    if os.path.isfile(file_path) and file_path[-3:] == 'txt':
        print("File was successfully retrieved")
    else:
        print("Cannot get file data. File is not a txt file or does not exist ")
        sys.exit()

    data = [0,0,0,0,0,0]
    fill_data(file_path, data)

    print("\nRESULT")
    print("===========================================================")
    print("Most used word: {}".format(data[MOST]))
    print("Least used word: {}".format(data[LEAST]))
    print("Longest word: {}".format(data[LONGEST]))
    print("Number of lines: {}".format(data[LINES]))
    print("Number of words: {}".format(data[NUMBER]))
    print("Number of characters: {}".format(data[CHARACTERS]))
    print("===========================================================")





