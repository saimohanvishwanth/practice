# a decorator is a function(or callable) that wraps another function(or class), modifying or enhancing its behavior without changing it source code.
#Syntax: commonly used with the "@decorator_name" pattern above the function to be decorated.
"""
def my_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)  # do something before
        return result # do something after
    #Usage:
    #---------

    @my_decorator
    def some_function():
        pass
    """
#Automotive-Focused ex
#Logging Decorator
"""
Scenario: you want to log the calls to a function that calculates fuel efficiency / speed

def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args} kwargs={kwargs}")
        result = func(*args,**kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper
    # apply the log_calls decorator toa fuel efficiency calculation function
@log_calls
def calculate_fuel_efficiency(distance_km, fuel_used_1):
    if fuel_used_1 == 0 :
        return None
    return distance_km / fuel_used_1

# test the decorated function

eff = calculate_fuel_efficiency(400, 20)   # output:Calling calculate_fuel_efficiency with args=(400, 20) kwargs={}
"""

#with out using decorator
"""
def func(f):
    def wrapper():
        print("Started")
        f()
        print("ended")
    return wrapper()

def func2():
    print("i am the functinon 2")

def func3():
    print("i am the functinon 3")

func3 =   func(func3)
func2 = func(func2)
func3()
func2()

"""

# with using decorator
# why(*args, **kwargs)? because we don't know how many arguments we are coming in here,rather than guessing for every single function
# whatever the arguments passed in wrapper function, it will go to arguments and keywordarguments

'''def func(f):
    def wrapper(*args, **kwargs):
        print("Started")
        rv = f(*args, **kwargs)
        print("ended")
        print("ended")
        return rv
    return wrapper()

@func
def func2(x,y):
    print("i am the functinon 2")

def func3():
    print("i am the functinon 3")

func3()
X = func2(4,10)
print(X)
'''
# while if we try to get / print the value of 2nd argument(y)
#in this case we need to store return value, so that i can return at the end of this wrapper
# instead of f(*args, **kwargs) we will assign it to rv -> rv = f(*args, **kwargs) and return rv at the end
# add functionality with out modifying code
#-----------------------------------------------------------------
#Timer decorators(for debugging, to check what is taking slowing down,logging(validate the input), how long it is going to take?
#--------------------
import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        rv = func()
        total = time.time() - start
        print("Time: ", total)
        return rv
    return wrapper

@timer
def test():
    for _ in range(50000):
        pass
@timer
def test2():
    time.sleep(2)

test()
test2()

