"""
Essential problems in Python; no.: 7
Objective: Verify if a string represents a valid numeric value (integer or float).
Author: Joydeep Pakira
"""
sentence = '1234a'

if sentence.replace('-', '').replace('.', '').isdigit():
    print("IsNumeric")
else:
    print("IsNotNumeric")
