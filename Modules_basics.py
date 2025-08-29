#Module is just a single python file(.py) that contains variables , functions / calsses you can use in other python programs

#ex: Creating a Moudle
'''
let's say you create a file named "car_utils.py".
#car_utils.py

def calculate_mpg(miles, gallons):
return miles / gallons

def start engine():
print("Engine started.")

#Using the Module in another file
#main.py

import car_utils
mpg = car_utils.calculate_mpg(300,10)
print(f"MPG: {mpg}")

car_utils.start_engine()

#Package
---------

a package is a directory(folder) that contains multiple modules and a special __init__ .py file.
It allows you to organize your modules logically.

Example folder structure:
automotive/

__init__.py # (initializing / empty)
engine.py
fuel.py
--------
*engine.py
def start_engine():
print("Engine started")
-----
fuel.py
def calculate_mpg(miles, gallons):
return miles / gallons
--------
main.py
from automotive import engine, fuel
engine.start_engine()
print(fuel.calculate_mpg(400, 10))    [o/p: engine started : 40.0]

Importing python libraries:
--------------------------

1. Os Module - Operating System Interface

used to interact with the file system and operating system tasks

example : Automotive log file Management

import os
# create a folder for acr diagnostics logs

if not os.path.exists("car_logs"):
    os.mkdir("car_logs")
    print("created folder: car_logs")
else:
    print("folder already exists")

2. Time Module - Time - related functions

# used to work with time delays, timestamps or performance tracking.

Ex: Simulate Engine Starting DELAY

import time
print("starting engine..")
time.sleep(2) # wait for 2 seconds
print("Engine started")

3. Sys Module - System -specific parameters & functions

#Used to interact with python run time environment.

Ex: Exit program if Mileage is invalid

import sys
mileage  = -100

if mileage < 0:
    print("Error : Mileage cannot be negative.")
    sys.exit() # stop the program if mileage is invalid
print("Mileage is valid")           [o/p: Error : Mileage cannot be negative.]
'''





