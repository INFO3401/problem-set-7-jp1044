# Collaborators: Taylor Lawrence, Marissa Kelley, Hannah Weber, Jack Sandberg
################################################################################
# PART #1
################################################################################
import os
import string
import csv
import json
import sqlite3

def countWordsUnstructured(filename):
    # This function should count the words in an unstructured text document
    # Inputs: A file name (string)
    # Outputs: A dictionary with the counts for each word
    # +1 bonus point for removing punctuation from the wordcounts
    file = open(filename)
    file_split = file.read().split()
    words = {}
    #print(file_split)
    for word in file_split:
        for mark in string.punctuation:
            word = word.replace(mark,"")
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

    #print(words)
    file.close()
    return words
# Test your part 1 code below.
#word_dict = countWordsUnstructured("state-of-the-union-corpus-1989-2017/Bush_1989.txt")
################################################################################
# PART 2
################################################################################

def generateSimpleCSV(targetfile, wordCounts):
    # This function should transform a dictionary containing word counts to a
    # CSV file. The first row of the CSV should be a header noting:
    # Word, Count
    # Inputs: A word count list and a name for the target file
    # Outputs: A new CSV file named targetfile containing the wordcount data
    file = open(targetfile, "w")
    file.write("Word,Count\n")
    for word, count in wordCounts.items():
        file.write(word + "," + str(count) + "\n")
    file.close()
    return

    # Test your part 2 code below
#generateSimpleCSV("test_file.csv",word_dict)
################################################################################
# PART 3
################################################################################
def countWordsMany(directory):
    # This function should create a dictionary of word count dictionaries
    # The dictionary should have one dictionary per file in the directory
    # Each entry in the dictionary should be a word count dictionary
    # Inputs: A directory containing a set of text files
    # Outputs: A dictionary containing a word count dictionary for each
    #          text file in the directory
    wordCountDict = {}
    dir_files = [entry.name for entry in os.scandir(directory)]
    for file in dir_files:
        wordCountDict[file] = countWordsUnstructured(directory+"/"+file)

    return wordCountDict

# Test your part 3 code below
#manyWordsDict = countWordsMany("./state-of-the-union-corpus-1989-2017")
#print(manyWordsDict)
################################################################################
# PART 4
################################################################################
def generateDirectoryCSV(wordCounts, targetfile):
    # This function should create a CSV containing the word counts generated in
    # part 3 with the header:
    # Filename, Word, Count
    # Inputs: A word count dictionary and a name for the target file
    # Outputs: A CSV file named targetfile containing the word count data
    outfile = open(targetfile, "w")
    outfile.write("Filename,Word,Count\n")
    for wordfile, dict in wordCounts.items():
        for word, count in dict.items():
            outfile.write(wordfile + "," + word + "," + str(count) + "\n")
    outfile.close()
    return 0
# Test your part 4 code below
################################################################################
# PART 5
################################################################################
def generateJSONFile(wordCounts, targetfile):
    # This function should create an containing the word counts generated in
    # part 3. Architect your JSON file such that the hierarchy will allow
    # the user to quickly navigate and compare word counts between files.
    # Inputs: A word count dictionary and a name for the target file
    # Outputs: An JSON file named targetfile containing the word count data
    outfile = open(targetfile, "w")
    outfile.write(str(wordCounts).replace("\'", "\""))
    outfile.close()

# Test your part 5 code below
    return 0
#generateJSONFile(manyWordsDict, "test_json.json")
################################################################################
# PART 6
################################################################################
def searchCSV(csvfile, word):
    # This function should search a CSV file from part 4 and find the filename
    # with the largest count of a specified word
    # Inputs: A CSV file to search and a word to search for
    # Outputs: The filename containing the highest count of the target word
    lines_processed = 0
    largest_count_file = ""
    largest_count = 0
    with open(csvfile) as csv_file:
        file = csv.reader(csv_file)
        for line in file:
            lines_processed += 1
            if line[1] == word and int(line[2]) > int(largest_count): # if the 2nd value in the line is the word we're looking for and larger than the current count
                largest_count = line[2]
                largest_count_file = line[0]
        csv_file.close()
    print("Data points processed:" + str(lines_processed))
    return largest_count_file

def searchJSON(JSONfile, word):
    # This function should search a JSON file from part 5 and find the filename
    # with the largest count of a specified word
    # Inputs: An JSON file to search and a word to search for
    # Outputs: The filename containing the highest count of the target word
    largest_count_file = ""
    largest_count = 0
    datapoints_processed = 0
    with open(JSONfile) as json_file:
        data = json.load(json_file)
        for file in data:
            datapoints_processed += 1
            if data[file][word] > largest_count:
                largest_count = data[file][word]
                largest_count_file = file
        json_file.close()
    print("Data points processed: " + str(datapoints_processed))
    return largest_count_file

# Test your part 6 code to find which file has the highest count of a given word
#print(searchCSV("test_csv_2.csv", "the"))
#print(searchJSON("test_json.json", "the"))

# +1 bonus point for figuring out how many datapoints you had to process to
# compute this value

def create_database(databaseName):
    #set up a connection to the database
    conn = sqlite3.connect(databaseName)
    c = conn.cursor()

    #Ask the connection to execute a SQL statement
    #Can't get the second query to run. Keep getting a "sqlite3.OperationalError: near "order": syntax error" error
    c.execute("CREATE TABLE word_counts(filename TEXT, word TEXT, count INTEGER)")
    c.execute("CREATE TABLE presidents_information(id INTEGER PRIMARY KEY, order INTEGER, start INTEGER, end INTEGER, president_name TEXT, prior_occupation TEXT, party TEXT, vice_president TEXT)")
    conn.commit()
    conn.close()


#create_database('presidents.db')
