# Modules in python. A module is a file containing python code that can be imported and reused into other modules.

# build-in-modules are modules that are included in the standard python library.
# Example: math, os, sys, etc.

import math

print(math.sqrt(16))
print(math.pi)

# import variations in python. 

# 1. import math    importing whole module
# 2. from math import sqrt   importing specific functions from a module
# 3. from math import *   importing all functions from a module 
# 4. import math as m   importing whole module with an alias

# Example:

# 1. os module. os module provides a way of interacting with the operating system.( files , directories, etc)
# 2. Json module. Json module provides a way of interacting with the json data. ( converting python objects to json and vice versa
# 3. datetime module. datetime module provides a way of interacting with the date and time. ( creating, formatting, parsing date and time
# 4. sys module. sys module provides a way of interacting with the system. ( command line arguments, exit, etc)

# os module example:
import os
print(os.getcwd())
print(os.listdir())
print(os.mkdir("test"))
print(os.rmdir("test"))


# Json module example:
import json
data={"name":"John","age":30,"city":"New York"}
print(data)
json_data=json.dumps(data)
print(json_data)

# datetime module example:
import datetime
print(datetime.datetime.now())
print(datetime.datetime.now().date())
print(datetime.datetime.now().time())

# sys module example:
import sys
print(sys.argv)
print(sys.version)
print(sys.exit())