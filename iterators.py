#Iterators : it is an object representing a stream of data, it returns data one element at a time when the next() function is called on it
# an object that enables a programmer to traverse a container, particularly lists
# we use the next function
#we didn't need to store the sequence in memory,we can generate the sequence as we want to loop through it.
#iterator protocol
'''
x = [1,2,3,4,5,6,7,8,9]
y = map(lambda x: x**2, x)
print(y.__next__())
while True:
    try:
        value = next(y)
        print(value)
    except StopIteration:
        print("Done")
        break

1. the object must have a __iter__() method running an iterator object
2. the iterator must have a __next__() method returning the next time
3. If no more items exist, __next__() should raise to StopIteration

EX: (SIMPLE)

Nump = [10,23.45,97]
#create an iterator object
iter_obj = iter(Nump)   # calls nums.__iter__()

#Acess elements one by one
print(next(iter_obj)),
print(next(iter_obj)),
print(next(iter_obj))
#next(iter_obj) now would raise Stop Iteration

Automotive ex:
#SIMULATED GEAR POSITIONS REPORTED OVER TIME
gear_positions = ['r','e' ,'y','t']

#create an iterator
gear_iter = iter(gear_positions)

#Acess each gear position in order
print(f"Current gear : {next(gear_iter)}")
print(f"Current gear : {next(gear_iter)}")
print(f"Current gear : {next(gear_iter)}")
print(f"Current gear : {next(gear_iter)}")

[o/p: Current gear : r
Current gear : e
Current gear : y
Current gear : t]

#Creating a custom Iterator
---------------------------
General syntax:
-----------

import sys
class Iter:
    def __init__(self, n):
        self.n = n
    def __iter__(self):
        self.current = -1
        return self
    def __next__(self):
        self.current +=1

        if self.current >= self.n:
            raise StopIteration
        return self.current

x = Iter(10)
itr = iter(x)
print(next(itr))
-------------
Scenario: you might want to iterate over a range of engine RPM values in a custom manner

class EngineRpmRange:
    def __init__(self, start, end, step):
        self.start = start
        self.end = end
        self.step = step
    def __iter__(self):
        self.current = self.start
        return self
    def __next__(self):
        if self.current> self.end:
            raise StopIteration
        else:
            rpm = self.current
            self.current += self.step
        return rpm
        return self.current
    #Create an EngineRpmRange object
engine_range = EngineRpmRange(1000, 3000, 500)
for rpm in engine_range:        #Use it in a for loop
  print(f"Current RPM: {rpm}")

[o/p: Current RPM: 1000
Current RPM: 1500
Current RPM: 2000
Current RPM: 2500
Current RPM: 3000 ]
'''

#Generators as a Simpler Alternative
#---------------

#Generators use yield keyword to produce an iterator without needing a class and maual __iter__()
#a routine that can be used to control the iteration behaviour of a loop.
#Generator is very similar to a function that returns an array
#When the yield key word hits,it pauses the execution of the function and returns this value, iterating through generator object

'''
from _pyrepl.commands import end
from turtledemo.penrose import start


def rpm_generator(start, end, step):
    rpm = start
    while rpm <= end:
        yield rpm
        rpm +=step
#Using the generator
for r in rpm_generator(1000, 3000, 500):
    print(f"Engine RPM: {r}")

[o/p: Engine RPM: 1000
Engine RPM: 1500
Engine RPM: 2000
Engine RPM: 2500
Engine RPM: 3000]

# when we use yield , it stops the function and returns Value (the RPM)
# we don't need to generate entire sequence
# you can sequence /large amount of data without need to store all of them
# you only need to know only current element, not before and after that element

another example : if you want to search the word in file which is having bunch / numerpous lines.
Generator : it will look if the word matches in current element/ row
Iterator: it will search before and after(next) element.
procedure: read entire file and loop it and use yield

import sys
def csv_reader(file_name):
    for row in open(file_name, "r"):
    yield row

key benefir: less bolierplate code than a custom iterator class

# Another way of creating generator with out keyword

x =(i for i in range(10))
for j in x:
    print(j)
'''
# generate a function and use yield function instead of return, it pauses the execution, it will continue whenever we call next function again.
# generator sysntax makes the next method and iter method implemented for us, so that we don't have to enter it manually write inside of the class
#Use case of a generator is , you can loop through a sequence/ a large amount of data without need to store all of them
# If you don't care about the function before or after the iteration
# You look for current piece of data,
import sys
"""def gen():
    yield 1
    print("Pause 1")
    yield 2
    print("Pause 2")
    yield 3
    print("Pause 3")
x= gen()
print(next(x))
print(next(x))
print(next(x))
"""

# if you have a millions fo line to present in the file, you gonna need only one particular row to search
# we can open the file like this
"""
import sys
def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row
"""
# we create the generator by comprhension
'''
x =(i for i in range(10))
for j in x:
    print(j)
'''
