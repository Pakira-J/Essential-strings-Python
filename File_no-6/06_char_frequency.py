"""
Essential problems in Python; no.: 6
Objective: Find how many times each character appears in a given string (ignore spaces).
Author: Joydeep Pakira
"""

from collections import Counter

phase = "The fossil belongs to a fish."

for key, value in Counter(phase.replace(' ', '')).items():
    print(f"{key} : {value}")
