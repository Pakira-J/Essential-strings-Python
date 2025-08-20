"""
Essential problems in Python; no.: 5
Objective: Replace every occurrence of "error" in a sentence (assume as a log file scenario) string with "warning".
Author: Joydeep Pakira
"""

log = "error occurred at step 3. Another error found."
print(log.replace('error', "warning"))
