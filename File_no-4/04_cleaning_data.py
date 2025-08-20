"""
Essential problems in Python; no.: 4
Objective: (i). Remove all leading/trailing spaces and convert a string to lowercase.
          (ii). Remove all spaces including spaces in between the sub-strings and convert a string to lowercase.
Author: Joydeep Pakira
"""

phase = " The fossil belongs to a fish "

# (i). Remove all leading/trailing spaces and convert a string to lowercase.
print(phase.strip().lower())

# (ii). Remove all spaces including spaces in between the sub-strings and convert a string to lowercase.
print(phase.replace(" ", "").lower())
