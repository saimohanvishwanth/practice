#Basic Unpacking( WE CAN DO IT WITH TUPLE, STRING)
"""a, b, c = [1, 2, 3]
print(f"a:{a}, b: {b}, c: {c}\n")"""
from fileinput import filename


#eXTENDED iterable unpacking with *
"""a, b, *c = [1,2,3,4,5,6]
print(f"a:{a}, b: {b}, c: {c}\n")"""

#Ignoring values
# When you need to put a variable somewhere but you don't actually want to access it later on, then we use "_"
#"_" - anonymous varilable
a,_,c = [1,2,3]


#Unpacking Nested Structures
"""data = ("Aline", (35, "Data_enginer"))
name,age , proffesion = data"""

#Unpacking Function Arguments
#"*names" - allows to collect any number of positional arguments

"""def print_names(*names):
    for name in names:
        print(name)
print_names("Alice", "Roxee", "Bubble" )

#Combining Lists with Unpacking
list_1 = [1,2,3]
list_2 = [4,5,6]
combined = [*list_1 , *list_2]
print(f"combined:{combined}\n")

#Unpacking Dicitionaries with **
dict1 = {"a": 1, "b" : 2}
dict2 = {"c": 3, "d" : 5}
combined_dict = {**dict1, **dict2}
print(f"Combined : {combined_dict}\n")

#Swapping Variable Using Unpacking
x = 10
y = 20
print(f"Before Swap - x: {x} , y : {y}")
x, y = y, x
print(f"After Swap - x: {x}, y: {y}\n")"""

#Eval function- little cautious while writing code
#Exec function - executes code in the current context of globles and locals
#here local variables/ functions are defined, we can able to access after the python code
#Exec doesn't return any value /result
# here we are defining function(exec()) inside the function(demonstrate_exec),
"""def  demonstrate_exec():
    code = "def greet(name):
    return f"Hello {name}\"
    exec(code)
"""
"""
    #Execute the code string
    # "Global Scope" -> entire python file "{}", the entire function, here starting from "demonstrate_exec()" till local variable/function
    # "Local Scope" -> Where it's executed - "()", the scope in which here execute this "exec" function
    local_scope = {}
    exec(code,{}, local_scope )
    print(local_scope["greet"]("Alice"))
#Eval - to access other pieces of code, you can all other functions and modify code from this evaluation
# "Eval' - is used for evaluating a single python expression
def demonstrate_eval():
    expression = input("Type an expression: ") #Evaluate the expression
    result = eval(expression)
    print(f"Result of eval: {result}")

#Defining what variables the user will have acess to , if theyr'e using eval function
def demonstrate_safe_eval():
    #Expression to evaluate
    expression = input("Type an expression that uses a, b and c: ")

    #Define variables for the expression
    variables ={ "a" : 1, "b" : 2, "c" : 3 }

    #Evaluate the expression in the context of the provided variables
    #Defining what this evaluation should have access to
    result = eval(expression, {}, variables)

    print(f"result of safe aval: {result}\n")

demonstrate_exec()"""

#Function and variable annotations:
#document the code while you write it
# good for yourself

name: str = "Alice"
age: int = 30
is_student: bool = False

#Function Annotations
# -> represents return
# Python can actually automatically pick that up and use it in a meaningful way
# the "First line" of a doc string is typically a short description of what the function does

def greet(person: str,age: int) -> str:
    """
    Greets a person  by name and age.
    :param person: The name of the person( expected to be a String)
    :param age: The age of the person (expected to be an integer).
    :return: A greeting message (expected to be a string).
    """

    return f"Hello , {person}! you are {age}, years old"

# Descriptor protocol
# Over writing the "__repr__" and "__str__" dunder methods
# Dunder method / double "__" methods ; these are hidden methods that activated, with in instance in the object
# always add while adding python classes such that they can be use anywhere
class Person:
    def __init__(self, name: str, age : int):
        self.name = name
        self.age = age
    def __repr__(self):
        """
        __repr__ is meant to provide an unambiguous string representation of the object.
        it's often used for debugging and should ideally return a string that could be used
        to recreate the object.
        """
        return f"Person(name -{self.name!r}, age={self.age})"

    def __str__(self):
        """
        __str__ is meant to provide a readable string representation of the object.
        it's what gets shown when you print the object or convert it to a string.
        :return:
        """
        return f"{self.name}, {self.age} years old"
# decorators
def my_decorator(func):
    """
    A simple decorator that prints a message before and after the execution of the function
    """
    def wrapper(*args, **kwargs):
        print("Before the function execution.")
        result = func(*args, **kwargs)
        print("After the function execution.")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    """
    a SIMPLE FUNCTION THAT GREETS THE USER
    """
    print(f"Hello, {name}!")

say_hello("Alice")

# what actual intention behind is ,"say_hello = my_decorator(say_hello)"

#Context Managers
# Handles the processing of the file whether it's opening, reordering,....etc.
# Automatically closing the file for you whether an error occurs or you're succesfully able to perform your operation
# with out having to do any thing too complicated
# you can contrl what happens when you are invoking and exiting a context
with open("test.txt","w") as file:
    file.write(" HI , i am back, how are you doing")

class FileManager:
    def __init__(Self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file =None

    def __enter__(self):
        #Open the file
        self.file = open(self.filename, self.mode)
        print(f"Opening file{self.filename}")
        return self.file

    def __exit__(self, exc_type, exc_val,exc_tb):
        # Close the file
        self.file.close()
        print(f"Closing file {self.filename}")
       #Handle exceptions, if needed
        if exc_type:
         print(f"An exception occured: {exc_val}")
        return True # Suppress exceptions, if needed

# iterators
# it is something that can provide sequence of values
# it is simple a python class that contains two dunder methods
#"__next__" -> gives the next value in a sequence
#"__iter__" -> set up the iterator and initialize all the value
#Next function-> will give you the next value from th ei

class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        #Initialize the current value here
        self.current = self.start


    def __iter__(self):
        """
        The __iter__ method makes this class an iterable.
        It should return an iterator object.
        """
        return self

    def __next__(self):
        """
        The __next__ method defines the iteration behavioiur.
        it should return the items in the sequence or raise StopIteration.
        """
        if self.current < self.end:
            value = self.current
            self.current +=1
            return value
        else:
            raise StopIteration
if __name__ == "__main__":
    y = MyRange(0,10)
    for x in y:
        print(x)

#Generators
#Modern version of Iterators, using by keyword "yield" in python function
#Yield keyword-> actually allows you to pause the execution of the function and only execute a little bit of code
#return a value and then pause and wait until , your'e asked for the next value to generate
# space efficient kind of execution or calculations to be done

    def count_up_to(max_value):
        """
        A generator function that yields numbers from 1 to max_value.
        :param max_value:
        :return:
        """
        current = 1
        while current <= max_value:
          yield current # Yield the current value and pause execution
          current +=1 #Increment the current value
# Generator -> can give us each value one by one and only store one value at a time when we need to use it.
    if __name__ == "__main__":
        counter = count_up_to(130000)
        print(next(counter))

        #iterate over the generator
        for number in counter:
            print(number)
# Once we yield a value , we actually pause the execution of the function and we wait at this yield line until the next value is requested

# Itertools:(advanced varsion of iteration)

import itertools

#Infinite iterators
counter = itertools.count(
    start =10, step =2
) #Infinite counterstarting at 10, increasing by 2
print(next(counter)) # o/p:- 10
print(next(counter)) #o/p:- 12(because we gave step as 2)

#Cycling through a finite sequence infintely
cycler = itertools.cycle(["A", "B", "C"])
print(next(cycler)) #O/p:- A
print(next(cycler))  #O/p:- B

#Creating combinations of elements
combinations = itertools.combinations("ABC",2)
print(list(combinations))

#Asynchronous
#Asynchronous programming is an easier way to handle multiple concurrent tasks rather than using something like threading
# asyncio library

import asyncio

#Define an asynchronous coroutine
# for ex:- for sending a network request, something that isn't really dependent on our computer/code.
#Wer're just waiting on something that we really don't have control over
# we don't know how long exactly it's going to take
# Asynchronous programming allows us to handle the timing of different events
# We can respond to things, when data comes in
# We can set up multiple different tasks and schedule those to run at the exact same time and allows us to more efficiently write code.









