#Lambda expression(anonymous function) in python is a small, inline function defined with the keyword lambda instead of def
#key characterisitics:
'''
no formal name
typically written in one line
often used for concise, short lived operations or when passing a function as an argument

Syntax:
lambda parameters: expression

parameters: optional, can be zero or more
expression: Must be a single expression(no statements)

Main use cases of lambda : map(), filter(), sort()
map()
---------
y = [1,2,3,4,5,6,3,4,9]

result_num = list(map(lambda x:x**2, y))
print(result_num)
--------
filter()
-----------
# Apply function to every single value inside of list/ierable object

my_numbers= [1,4,6,8,9,23,12,45]

evens = list(filter(lambda x:x%2==0, my_numbers))
print(evens)
---------
Sort()
-------------
values = [(1,'b',"hello"),(2,'a',"welcome"),(3,'t',"our home")]
resultant = sorted(values,key = lambda x: x[0])
print(resultant)
----------
reduce()
#it's going to reduce down some kind of iterable object to a single value

from functools import reduce

number = [1,4,5,7,9,10]
# 1+4 =5
# 5+5 = 10
# 10+7 = 17
# 17+9 = 26
# 26 + 10 = 36

#using reduce to sum the list without initializer
sum_of_numbers = reduce(lambda acc, x: acc + x, number)
print(sum_of_numbers) # output =36

#Using reduce functoin to find the maximum value

max_value = reduce(lambda acc, x: acc if acc>x else x, number)
print(max_value) #output = 10

fancy_comp = {x:(lambda x: x*x)(x) for x in range(5)}
print(fancy_comp) #output:{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

 Ex:
#Simple lambda that squaers a number
square = lambda x: x *x

#Using the lambda
print(square(5)) # output: 25

Common use cases
#1. Sorting with a custom key
#---------------------
#List of vehicles with their speeds
vehicles = [("car", 120),("Truck", 80), ("MOtorCycle", 190)]

#Sort vehicles by speed using a lambda function
vehicles.sort(key = lambda v: v[1])

#Print the sorted list
print(vehicles)          # output :[('Truck', 80), ('car', 120), ('MOtorCycle', 190)]

2. Filtering or Mapping
#----------------------

#list of speeds
speeds = [50, 100, 150, 200]

#use filter with lambda to select speeds greater than 120
fast_speeds = list(filter(lambda s : s>120, speeds))

#print the filtered list
print(fast_speeds)  #output: [150, 200]

# Automotive Example

Scenario: we want to quickly filter sensor readings above a threshold without writing a separate function.

# list of sensor readings( ex: temperature or pressure values)
sensor_Readings = [12.4,13.9,20,14.2,11,14.3]

#Filter readings above 12.0 using a lambda function
above_12 = list(filter(lambda r:r>12.0,sensor_Readings))

#print the filtered readings
print(above_12) # [o/p : [12.4, 13.9, 20, 14.2, 14.3]]
'''
# here a lambda is used to define the conditoin r>12




