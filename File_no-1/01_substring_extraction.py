"""
Essential problems in Python; no.: 1
Objective: Given string: s = "PythonAutomation", extract "Automation" using slicing.
Author: Joydeep Pakira
"""

s = "PythonAutomation"
print(s[6:])

# Below block, funtions the same as that of slicing but the method use here is index()
for i in s:
    if i == "A":
        # used to fetch the index of "A" from where the slicing is to be done.
        s.index(i)
        break

print(s[s.index(i):])
