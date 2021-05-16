import linecache
import random

randAdj = random.randint(1 , 228)
randNoun = random.randint(232 , 603)
randVerb = random.randint(606 , 2109)
randAdverb = random.randint(2112 , 2441)

Adjective = linecache.getline('source.txt',randAdj)
Noun = linecache.getline('source.txt',randNoun)
Verb = linecache.getline('source.txt',randVerb)
Adverb = linecache.getline('source.txt',randAdverb)

password = str(Adjective) + str(Noun) + str(Verb) + str(Adverb) #puts string to together
password = str.join(" ", password.splitlines()) #puts it all on the same line
password = password.replace(" ", "") #takes all white space out
password = password.lower() #converts all to lower case

print("password: " + str(password))
