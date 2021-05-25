import linecache
import random
import os
import sys
import hashlib
from cryptography.fernet import Fernet

key = b'3rjnDPiSE5NLPBInYz1A8qw1eRbZncJLMcO5imPaUZU=' # THIS IS TEMPORERY
cipherKey = Fernet(key)

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

file = open("masterpassword.txt","r")
masterPassword = file.read()
file.close()
if masterPassword == "": #no master password
    masterPassword = input("Please input a new master password: ") #input master password
    masterPassword = hashlib.md5(masterPassword.encode())
    masterPassword = masterPassword.hexdigest() #hash it
    file = open("masterpassword.txt","a")
    file.write("masterpassword: " + masterPassword) #saves it ti masterpassword.txt
    file.close()
else: #if somthing in masterpassword.txt
    check = input("Please input master password: ") #input master password
    throwaway, masterPassword = masterPassword.split(" ") #takes the hash from pasword.txt
    check = hashlib.md5(check.encode())
    check = check.hexdigest() #hashes check
    while str(check) != str(masterPassword): #if password is wrong
        check = input("Please input master password: ") # askes again
        check = hashlib.md5(check.encode())
        check = check.hexdigest() #hashes the new input 
        if str(check) == str(masterPassword): #if password is correct contue
            continue


while True:
    inputVar = input("What do you want: ")

    #what do you want

    #adds new password
    if inputVar == "new password": 
        newName = input("Name: ") #lets you set name
        newPwd = input("Password: ") #lets you set password
        if newPwd == "random":
            newPwd = randPwd()
        newPwdEnc = newPwd.encrypt(b"A really secret message. Not for prying eyes.") # encrypts
        file = open("passwordstore.txt", "a")
        file.write("\nNAME: " + str(newName) + " --- PASSWORD: " + str(newPwdEnc) + "\n")
        file.close()

    #clears all password
    elif inputVar == "clear": 
        yorn = input("Are you sure you want to do this, it cannot be undone: Y or N: ")
        if yorn == "Y" or yorn == "y":
            file = open("passwordstore.txt", "w")
            file.write("")
            file.close()
            print("cleard")

    #quits program
    elif inputVar == "quit": 
        print("quitting...")
        quit()

    #prints all
    elif inputVar == "print all": #prints all
        file = open("passwordstore.txt", "r")
        print(file.read())
        file.close()

    #genorates random password
    elif inputVar == "random password": 
        print(randPwd())
    
    # helps you
    elif inputVar == "help":
        print("   -new password: lets you add new password")
        print("   -random password: generates random password (if you set your password world to random it will generate a random one in its place)")
        print("   -print all: prints all passwords")
        print("   -find password: searches for a file of your choice")
        print("   -quit: quits program")
    
    #searches file for name
    elif inputVar == "find password":
        findName = input("what is the password named: ")
        with open('passwordstore.txt', 'r') as searchfile: 
            for line in searchfile:
                if findName in line: #searches for input
                    print(" ")
                    line = cipherKey.decrypt(line) # decrypts
                    print(line)
    
    elif inputVar == "delete password":
         delete = input("what is the name of the password you want to delete: ")
         with open('passwordstore.txt', 'r') as searchfile: 
            for line in searchfile:
                if delete in line: #searches for input
                    file = open("passwordstore.txt.txt", "w")
                    lines = delete
                    for line in lines:
                        if line.strip("\n") != "line2":
                            file.write(line)
                        file.close()
