"""
Essential problems in Python; no.: 9
Objective: Given Mask all except the last 4 character of a given serial number string.
Author: Joydeep Pakira
"""

serial_no = "7263455786ABDC"

# Masking all the characters except the last four characters:
print("*" * (len(serial_no) - 4), serial_no[-4:])

# Masking last four characters only:
print("****" .join(serial_no.split((serial_no[(len(serial_no) - 4):]))))
