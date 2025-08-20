"""
Essential problems in Python; no.: 10
Objective: From "Reading: temp=30C voltage=220V", 
           extract numeric values and store them in a list as integers.
Author: Joydeep Pakira
"""

import re
s = "Reading: temp=30C voltage=220V"
nums = re.findall(r'\d+', s)
nums = list(map(int, nums))
print(nums)
