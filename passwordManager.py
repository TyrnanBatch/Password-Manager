import linecache
import random
import os
import sys

def randPwd():
    randAdj = random.randint(2 , 229)
    randNoun = random.randint(233 , 604)
    randVerb = random.randint(607 , 2110)
    randAdverb = random.randint(2113 , 2442)

    Adjective = linecache.getline('source.txt',randAdj)
    Noun = linecache.getline('source.txt',randNoun)
    Verb = linecache.getline('source.txt',randVerb)
    Adverb = linecache.getline('source.txt',randAdverb)

    password = str(Adjective) + str(Noun) + str(Verb) + str(Adverb) #puts string to together
    password = str.join(" ", password.splitlines()) #puts it all on the same line
    password = password.replace(" ", "") #takes all white space out
    password = password.lower() #converts all to lower case
    
    return password

inputVar = input("What do you want: ")

if inputVar == "password":
    print(randPwd())

if inputVar == "new password":
    newName = input("Name: ")
    newPwd = input("Password: ")
    if newPwd == "random":
        newPwd = randPwd()
    file = open("passwordstore.txt", "a")
    file.write("\nNAME: " + newName + " --- PASSWORD: " + newPwd + "\n")
    file.close()

elif inputVar == "clear":
    yorn = input("Are you sure you want to do this, it cannot be undone: Y or N: ")
    if yorn == "Y" or yorn == "y":
        file = open("passwordstore.txt", "w")
        file.write("")
        file.close()
        print("cleard")

elif inputVar == "quit":
    quit()
elif inputVar == "print all":
    file = open("passwordstore.txt", "r")
    print(file.read())
    file.close()

with open('passwordstore.txt', 'r') as searchfile:
    for line in searchfile:
        if inputVar in line: #searches for input
            print("line")



os.execl(sys.executable, sys.executable, *sys.argv) #restarts program
