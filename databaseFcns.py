# Place any necessary imports here
import sqlite3

####################################################
# Part 0
####################################################

# Move your parsers.py file to your Problem Set 7
# directory. Once you've done so, you can use the
# following code to have access to all of your parsing
# functions. You can access these functions using the
# parsers.<function name> notation as in:
# parsers.countWordsUnstructured('./state-of-the-union-corpus-1989-2017/Bush_1989.txt')
import parsers

####################################################
# Part 1
####################################################

def populateDatabase(databaseName, wordCounts, metaData):
    # Write a function that will populate your database
    # with the contents of the word counts and us_presidents.csv
    # to your database.
    # Inputs: A string containing the filepath to your database,
    #         A word count dictionary containing wordcounts for
    #         each file in a directory,
    #         A metadata file containing a dictionary of data
    #         extracted from a supplemental file
    # Outputs: None
    conn = sqlite3.connect(databaseName)
    c = conn.cursor()
    for file in wordCounts:
        for word in wordCounts[file]:
            print(word)
            c.execute('''INSERT INTO word_counts (filename,word,count) values (:file,:word,:count)''',{'file' : file,'word': word,'count': wordCounts[file][word]})
    c.execute('''SELECT word FROM word_counts''')
    print(c.fetchall())
    with open("us_presidents.csv") as presidents_csv:
        data = csv.reader(presidents.csv)
        for row in data[1:]:
                c.execute('''INSERT INTO presidents_information (index,order,start,end,president_name,prior_occupation,party, vice_president) values ({0},{1},{2},{3},{4},{5},{6},{7})'''.format(row[0], row[1], row[2], row[3], row[4],row[5], row[6], row[7]))

    return 0

# Test your code here
# Cannot create the database because of errors
parsers.create_database("presidents.db")
populateDatabase("presidents.db", parsers.countWordsMany("./state-of-the-union-corpus-1989-2017"), "us_presidents.csv")
####################################################
# Part 2
####################################################

def searchDatabase(databaseName, word):
    # Write a function that will query the database to find the
    # president whose speech had the largest count of a specified word.
    # Inputs: A database file to search and a word to search for
    # Outputs: The name of the president whose speech contained
    #          the highest count of the target word
    return 0

def computeLengthByParty(databaseName):
    # Write a function that will query the database to find the
    # average length (number of words) of a speech by presidents
    # of the two major political parties.
    # Inputs: A database file to search and a word to search for
    # Outputs: The average speech length for presidents of each
    #          of the two major political parties.
    return 0
