# Kat Wayman
# Due Date: March 5, 2023
# Course: CS 457
# Project: Programming assignment 1
# Description: the purpose of this program is to simulate 
# a more simplified version of an SQL database using 
# python. this means to add delete the databases, tables, 
# and to change their attributes
  
import os as main
import subprocess as argument


databaseWorks = None
TableList = [None]
userInput = None


#code to remove semi colon for readability
def clean(extraChar):
  query = userInput.replace(";", "")
  return query.replace(extraChar, "")

#code to test if the database already exists
def databaseTest(dataBase):
  if dataBase in argument.run(['|', dataBase], capture_output=True, text=True).stdout:
    return 1
  else:
    return 0

# runs a test if a table already exists under that name
def tableTest(table):
  if table in argument.run([ databaseWorks,  '|', table], capture_output=True, text=True).stdout:
    return 1
  else:
    return 0

# code to quit the program
while (userInput != ".EXIT"):
    userInput = input("")
    if (userInput == ".EXIT"):
        print("All done.")
        exit()
  
# creates database
    elif ("CREATE DATABASE" in userInput):
        dataBaseName = clean("CREATE DATABASE ")
        if databaseTest(dataBaseName) == 0:
            main.system(f'mkdir {dataBaseName}')
            print(f"Database {dataBaseName} created.")
        else:
            print(f"!Failed to delete {dataBaseName} because it already exists.")
  
# deletes database
    elif ("DROP DATABASE" in userInput):
        dataBaseName = clean("DROP DATABASE ")
        if databaseTest(dataBaseName):
            main.system(f'rm -r {dataBaseName}')
            print(f"Database {dataBaseName} deleted.")
        else:
            print(f"!Failed to delete {dataBaseName} because it does not exist.")
  
# opens selected database
    elif ("USE" in userInput):
        databaseWorks = clean("USE ")
        if databaseTest(databaseWorks):
            print(f"Using database {databaseWorks}.")

# creates a table with userinput
    elif ("CREATE TABLE" in userInput):
        # used to seperate into different strings for usage
        tableInput = clean("CREATE TABLE ")
        tableName = tableInput.split()[0] # collects table name
        tableRest = tableInput.replace(tableName, "")
        tableAttributeEmpty = tableRest[2:] # removes name for arguments
        tableAttributeCreated = tableAttributeEmpty[:-1] # 
        tableAttributes = tableAttributeCreated.split(",") # used to create a list of attributes

        if (databaseWorks != None):
            if tableTest(tableName) == 0:
                main.system(f'touch {databaseWorks}/{tableName}.txt')
                filename = databaseWorks + '/' + tableName + '.txt'
                f = open(filename, 'w')
                f.write(" |".join(tableAttributes)) # puts the table attributes into a file
                f.close()
                print(f"Table {tableName} created.")
            else:
                print(f"!Failed to create table {tableName} because it already exists.")

# deletes table
    elif ("DROP TABLE" in userInput):
        tableName = clean("DROP TABLE ")
        if (databaseWorks != None):
            if tableTest(tableName):
                main.system(f'rm {databaseWorks}/{tableName}.txt')
                print(f"Table {tableName} deleted.")
            else:
                print(f"!Failed to delete {tableName} because it does not exist.")
    
# used to output what is in that table
    elif ("SELECT *" in userInput):
        selection = clean("SELECT * FROM ")
        if databaseWorks != None:
            if tableTest(selection):
                f = open(f'{databaseWorks}/{selection}.txt', 'r')
                print(f.read())
                f.close()
            else:
                print(f"!Failed to query table {selection} because it does not exist.")

# used to change information in a table
    elif ("ALTER TABLE" in userInput):
        alter = clean("ALTER TABLE ")
        tableName = alter.split()[0]
        alterCommand = alter.split()[1]
        alterVar1 = alter.replace(tableName, "")
        alterVar2 = alterVar1.replace(alterCommand, "") 
        newAttribute = alterVar2[2:]

        if databaseWorks != None:
            if tableTest(tableName):
                f = open(f'{databaseWorks}/{tableName}.txt', 'a')
                f.write(f" | {newAttribute}")
                f.close()
                print(f"Table {tableName} Modified.")
                
quit()
