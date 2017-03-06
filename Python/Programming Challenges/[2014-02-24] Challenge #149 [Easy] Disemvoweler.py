__author__ = 'alex.taxter'
'''
https://www.reddit.com/r/dailyprogrammer/comments/1ystvb/022414_challenge_149_easy_disemvoweler/
'''

import re,sys

t = input("Enter string: ").replace(" ","")

print(re.sub('[aeiou]','',t))
print(re.sub('[^aeiou]','',t))