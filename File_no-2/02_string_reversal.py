"""
Essential problems in Python; no.: 2
Objective: Reverse a string without using 'reversed()' or '::-1'
Author: Joydeep Pakira
"""

word = "meghalaya"

# converting string into list and then reversing using pop() method
dummy = list(word)
for i in range(len(dummy)):
    print(dummy.pop(), end='')

# Alternate method: using string formatting only
rev = ""
for char in word:
    rev = char + rev

print("\n"+rev)
