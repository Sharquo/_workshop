__author__ = 'alex.taxter'
'''
https://www.reddit.com/r/dailyprogrammer/comments/3ofsyb/20151012_challenge_236_easy_random_bag_system/
'''

import random

# create the tetris pieces

def makeTetris():
    pieces = ["O", "I", "S", "Z", "L", "J", "T"]
    string = ""
    for i in range(7):
        random.shuffle(pieces)
        string += "".join(pieces)
    string += pieces[random.randint(0,6)]
    return(string)

# verification

def verification(inp):
    for i in range(1,8):
        chunk = inp[(7*(i-1)):(i*7)]
        pieces = ""
        for c in chunk:
            if c in pieces:
                return("invalid")
            break
        else:
            pieces += c
    else:
        return("valid")