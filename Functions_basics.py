#Functions
'''
Re usable block of code that performs a specific task
you define a function once and call it whenever you need it

# to define a function
syntax:
def greeet():
print("look here")

this defines a simple functions named greeet that takes no arguments and prints  a message

#Automotive ex: Print CAR brand

# define he function
_______________________

def show_car_brand(brand):
    print(f"car brand" is {brand}.")

#Call the function
---------------------

show_car_brand("Hyundai")
Show_Car_brand("BMW')

# TO call function, just its name followed by parenthess:

#Function with parameters
-------------------------
u can pass data to a function using parameters:

def greet(name):
print("Hello, {name})!")

#Call it like this:
greet('Alice')

Output:
Helloe Alice

#Single Parameter ex:
-----------------------
it accepts one argument and performs some operation.

ex: Calculate car speed

def car_speed(distance):

#Assuming the car takes 2 hours to travel the distance
speed = distance/2
return speed

Function call:
----------------

speed = car_speed(100) # 100 miles
print(f"the car's speed is {speed} mph.")       [o/p: the car's speed is 50.0mph.

Double Parameters EX:
----------------------

function with 2 parameters can accept two values and use them together to perform an operation
-----------------------------

def calculater_mpg(miles, gallons):
if gallons == 0:
return "Error : Gallons used cannot be zero"
return miles / gallons

#Function Call

mpg = calculate_mpg(300,10) # 300 miles, 10 gallons
print(f'Fuel Effficiency : {mpg} MPG")              [o/P: Fuel efficiency : 30.0 MPG

Multiple Parameters EX:
-----------------------

When a function accepts multiple parameters, it can handle more complex operations

EX:n Start a car Engine with Options

def start_car(model, engine_type, color ='Red'):
print(f"Starting the {color} {model} with a {engine_type} engine.")

Function CALL:

start_Car("Hinda Civic", "petrol") # use default color "Red"
start_Car("Tesla", "electric", "Blue")

#Functions can return a value using return keyword:

def add(a,b):
return a+b

#Call and store the result:
result = add(5,3)
print(result)    [o/p: 8]

#Automotive Example: Calculate Fuel Cost
1. define the function

def calculate_fuel_cost(liters, price_per_liter):
total_cost = liters * price_per_liter
return total_cost

2. call the function and store the result

cost = calculate_fuel_cost(40, 1.5)
print(f"the total uel cost is ${cost:.2f}")  [o/p : the total fuel cost is $60.00

# Default Parameter Values

you can provide default values for parameters

def greet(name = 'friend'):
print(f"hello, {name}!")
greet                                       [o/p : hello, luna!

#Automotive Example:Start a car with Optional Engine Type

1. define the Function with Default parameter
def start_car(brand, engine_type = 'petrol'):
print(f"Starting the {brand} with a { engine_type} engine.")

2. Call the function(with and with out the optional argument)

start_car("Toyota") # uses default : petrol
start_Car("Tesl", "electric")             O/p:STARTING THE Toyota with a petrol engine


#Use cases: fuel efficiency calculators, DTC LOOKUP TOOLS

In real-world use cases like fuel efficiency calculators and DTC(diagnostics trouble code) lookup tools implemented as python functions

1. Fuel Efficiency CALCULATOR(MPG)

function: calculate_mpg()


def calculate_mpg(miles_driven, gallons_used):
    if gallons_used == 0:
        return 'Error: Gallons used cannot be zero'
    mpg = miles_driven / gallons_used
    return round(mpg, 2)

efficiency = calculate_mpg(300, 10)
print(f"Fuel Efficiency: {efficiency} MPG")

# [O/P: Fuel efficiency : 30.0 MPG]

2. DTC(Diagnostic Trouble Code) Look up tool
Function: lookup_dtc()

def lookup_dtc(code):
    dtc_codes = {
           "P0300": "Random/Multiple Cylinder Misfire Detected",
            "P0171": "System too lean (Bank 1)",
            "P0420": "Catalyst System Efficiency Below Threshold( Bank 1)",
            "P0455" : "Evaporative Emission Control system leak detected (large leak)"}
    return dtc_codes.get(code.upper(), "DTC CODE not found.")

#Example Usage:
dtc_description = lookup_dtc("P0300")
print(f"DTC Description : {dtc_description}")   #o/p:DTC Description : Random/Multiple Cylinder Misfire Detected'''

