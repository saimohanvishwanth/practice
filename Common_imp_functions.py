#1.Print()
# general view we will see without improving and after improving

#Generally
'''
age = 23
name = ("Tim")
print("My name is ", name, "and i am ", age,"years old")
# we can pass additional arguments to print function
print("My name is ", name, "and i am ", age,"years old", sep="|")
print("My name is ", name, "and i am ", age,"years old", sep =",")
print("My name is ", name, "and i am ", age,"years old", sep ="\n")
print("My name is ", name, "and i am ", age,"years old", end = "| ")
'''
#help() - allows to print ou the documentation of python function
'''# useful for built in functions,when you are working with library written by other people
def upperndra(a, b):
    """
    a: value 1
    b: value 2
    c : value 3

    return int

    """
    return a+ b

help(upperndra)
#output: upperndra(a, b)
    a: value 1
    b: value 2
    c : value 3

    return int
'''
#Range: iterate bunch of values , generate a list of numbers

"""rng = range(2,10, 2)
#range(start, end, step)
print(list(rng))"""

#Map:allows to apply a functionto every element in iterable object
'''strings = ["my", "wrold", "apple", "pear"]
my_list_1 = [1,2,3,4,5]
my_tuple_1 = (1,2,3,4,5)

#lengths = map(len, strings)
#lengths = map(lambda x: x +'s', strings)
def add_s(string):
    return string + 's'

lengths = map(add_s, strings)
print(list(lengths))'''

#Filter: it will take all items in the iterable object the nit pass it to compatible function
'''
def longer_than_4(string):
    return len(string)> 4
strings = ["my", "wrold", "apple", "pear"]
#filtered_string = filter(longer_than_4, strings)
filtered_string=filter(lambda x:len(x) > 4, strings)
print(list(filtered_string))
'''
#sum()- return the sum of the all different numbers in iterable object
'''numbers = {1,2,3,4.5, 43, 78, 98}
#print(sum(numbers))
print(sum(numbers, start=-10))'''

#sorted()- sort an iterable object in ascending order
#-----------------
'''
numbers = [4,5,6,7,-2,0,4.6]
#sorted_nums = sorted(numbers)
#sorted_nums = sorted(numbers, reverse =True)
sorted_nums = sorted(numbers, reverse =True,key=abs)
print(sorted_nums)

people = [{"name": "Alice","age": 30},{"name": "Alex","age": 20},{"name": "Aernd","age": 23}]

sorted_people = sorted(people, key=lambda person: person['age'], reverse=False)
print(sorted_people)'''

#enumerate()-
#-----------------------
#case 1: with out enumerate
tasks = ["Write report", "atternd class", "review meeting", "submit code"]
"""for index in range(len(tasks)):
    task = tasks[index]
    print(f"{index + 1}.{task}")"""
#case 2: with enumerate ()- in below 1st variable would be index and 2nd would be the value
'''for index, task in enumerate(tasks):
    print(f"{index +1}.{task}")'''
#case3 : with out for loop
#print(list(enumerate(tasks)))

#ZIP():
#--------------
#case 1: with out using ZIP()
'''names=["Alice", "Bob", "Charlie", "David"]
ages = [30,25,45,20]
# the reason behind the adding len() is , here we have more values in  names than ages
for idx in range(min(len(names), len(ages))):
    name = names[idx]
    age = ages[idx]
    print(f"{name}is {age} years old")'''

#case 2:
# using zip function: combine iterable objects together automatically handle when one iterable object has more objects than other
"""names = ["Alice", "Bob", "Charlie","tim", "David"]
ages = [30,25,45,20]
genders = ['Female', 'Male','Male']

combined = list(zip(names, ages, genders))
for name, age, gender in combined:
    print(f"{name} is {age} years old and is {gender} gender")"""

#Open() -  open afile read to it, write to it
file = open("test.txt","w")
file.write("hello, mowa\n my name is vishwanth")
file.close()
# another format
with open("test.txt", "r") as file:
    text = file.read()
    print(text)
with open("test.txt", "a") as file:
    file.write("I will be back soon, get ready")

