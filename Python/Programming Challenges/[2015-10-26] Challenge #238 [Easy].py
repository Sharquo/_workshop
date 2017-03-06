__author__ = 'alex.taxter'
'''
https://www.reddit.com/r/dailyprogrammer/comments/3q9vpn/20151026_challenge_238_easy_consonants_and_vowels/
'''

import random

def randword(cv):
    randword = ""
    keys = {'c': "bcdfghjklmnpqrstvwxyz", 'v': "aeiou"}
    for i in cv:
        if i.lower() in keys:
            randword = randword + str(random.choice(keys[i.lower()]))
        else:
            break
    else:
        return randword
    return None

while True:
    pattern = randword(input("Enter pattern, or type 'Quit' to quit: "))
    if not pattern is None:
        print (pattern, "\n")
    else:
        print("Please only enter c or v characters. \n")