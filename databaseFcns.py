# Place any necessary imports here
import sqlite3
import csv
import pandas as pd

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
            c.execute('''INSERT INTO Word_counts (filename,president,year,word,count) values (:file,:president,:year,:word,:count)''',{'file' : file,'president':file.split('_')[0],'year':file.split('_')[1].split('.')[0],'word': word,'count': wordCounts[file][word]})
    with open("us_presidents.csv", encoding = "latin1") as presidents_csv:
        data = csv.reader(presidents_csv)
        for idx, row in enumerate(data):
            if idx != 0:
                firstName = row[4].split(" ")[0]
                lastName = row[4].split(" ")[-1]
                c.execute('''INSERT INTO Presidents_information (id,test,start,end,president_firstname,president_lastname,prior_occupation,party, vice_president) values (?,?,?,?,?,?,?,?,?)''',(row[0],row[1],row[2],row[3],firstName,lastName,row[5],row[6],row[7]))
    c.execute("SELECT * FROM Word_counts")
    print(c.fetchone())
    c.execute("SELECT * FROM Presidents_information")
    print(c.fetchone())
    conn.close()
    return 0

# Test your code here
# Cannot create the database because of errors
parsers.create_database("presidents-2.db")
populateDatabase("presidents-2.db", parsers.countWordsMany("./state-of-the-union-corpus-1989-2017"), "us_presidents.csv")
####################################################
# Part 2
####################################################

def searchDatabase(databaseName, word):
    # Write a function that will query the database to find the
    # president whose speech had the largest count of a specified word.
    # Inputs: A database file to search and a word to search for
    # Outputs: The name of the president whose speech contained
    #          the highest count of the target word
    conn = sqlite3.connect(databaseName)
    c = conn.cursor()
    #Returns None, but Syntax
    c.execute('''SELECT MAX(count) FROM Word_counts WHERE word = :word''', {'word' : word})
    word = c.fetchone()
    conn.close()
    return word
print(searchDatabase("presidents-2.db", "the"))
def computeLengthByParty(databaseName):
    # Write a function that will query the database to find the
    # average length (number of words) of a speech by presidents
    # of the two major political parties.
    # Inputs: A database file to search and a word to search for
    # Outputs: The average speech length for presidents of each
    #          of the two major political parties.
    conn = sqlite3.connect(databaseName)
    c = conn.cursor()
    #Started to join on president name and year, but presidents names need to be separated out, which I was having trouble
    #getting to work
    #pd.read_sql('''SELECT Presidents_information.party, Word_counts.year, Word_counts.word, Word_counts.count FROM Word_counts FULL OUTER JOIN Presidents_information ON Word_counts.year=''')
    return 0
