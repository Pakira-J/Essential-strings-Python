"""
Essential problems in Python; no.: 8
Objective: Given "sensor1, sensor2, sensor3", convert it into a list, add one more sensor and rejoin it into a list.
Author: Joydeep Pakira
"""

sensor = "sensor1, sensor2, sensor3"
sensor_list = sensor.split(', ')
sensor_list.append('sensor4')
print(", ".join(sensor_list))
