#Exercise 2: Good Morning Sir
#Author: Naina Mogha
#Date : 30 June 2024
#Create a python program capable of greeting you with Good Morning,
#Good Afternoon and Good Evening. Your program should use time module to
#get the current hour. 

import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)
