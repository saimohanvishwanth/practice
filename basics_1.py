#Variables in Python
a = 'This'
b = 'is'
c = 'Automotive python training'
vehicle_speed = 90
baud_rate = 2500000000
fuel_efficiency = 16.5
enginer_Status = True
door_locked = False
# lists ordered , changeable, and allows duplicates. A list is ued to store multiple values in a single variable."[]", you can add, remove, or change items in a list.
sensor_names = ['Radar', 'Lidar', 'Ultrasonic_sensor']
vehicle_models = ['sedan','SUV', 'Truck', 'Convertaible']
# append,
'''
sensor_names[1] = "Front Lidar"
sensor_names.append('infrared')
'''
print(vehicle_speed)
print(a +" "+b+ " "+c)
#Tuples :- Ordered, unchangeable,and allows duplicates."()".You can't change it's values after creation.
ecu_versions = ("v1","v2","v3")
#dictionaries :- Unordered , changeable, and uses key- value pairs
#{}
# ideal for mapping data like sensor names to values, DTC codes to descriptions....etc.
vehicle_data = {'speed': 120, "fuel_level":12, "engine_Status": 'On',"Gear":3}
#Operators:- perform operations variables and values
'''
fuel_efficiency = distance_traveled_lm/fuel_used_liters
total_fuel_cost = fuel_used_liters * fuel_price_per_liter
cost_per_km = total_fuel_cost / distance_traveled
'''
fuellevel = 9
enginestatus = 1
batterylevel = 8
if fuellevel < 10 and enginestatus == 1 or  fuellevel <10 or  batterylevel < 10:
    print("critical:low fuel with engine ON!")
    print("check vehicle:low fuel or low battery!")
# Conditional statements
#if else elif
# saftey checks (speeding, engine overheating)
# System states:(fuel sensor functionality, door open/closed)
'''
#Speed Monitoring 
speed_kmh = 120
if speed_kmh > 120:
    print("Overspeed")
elif speed_lmh >= 80:
    print("With in highwa speed range ")
else:
    print("Below minimum speed limit")
the code checks if speed exceeds a thrshold , is iwth in a range
'''
#Temperature-Based WARNING
'''engine_temp = 105.5

if engine_temp > 100:
    print("warning: High Engine Temperature")
elif engine_temp > 90:
    print("Engine temperature slightly elevated")
else:
    print("Engine temperature normal")

different message display based on how high the temperature is 
'''
#Fuel Checking
'''
fuel_level = 3.2 #liters
fuel_sensor_ok = True

if fuel_sensor_ok == False:
    print("Fuel sensor offline.Cannot determine fuel level")
elif fuel_level < 5:
    print("Fuel sensor offline. cannot determine fuel level")
else:
    print("Low fuel alert")
'''
#Nested Conditionals
# you can place if statements inside another if block , though you should do so only if it logically benefits clarity
'''Speed = 90
is_raining = True

if speed < 120:
    if is_raining:
        print("Drive with caution, reduce speed further due to rain")
    else:
        print("safe speed continue.")
'''
#While loop
# loop repeates a block of code as long as certain condition remains True
#once tht condition becomes False or you manually break out of the loop, the loop terminates
#Synatax
#While Condition
# Code to request
'''
Check the condition: if it's true, enter the loop.run the code block
recheck the condition at the end of each iteration.
if the condition is still true , continue, if it's false, exit the loop

ex(simple counter);

count = 0
while count <5
printf(f'conatnt is {count})
count+=1 # increment count

this prints count is 0 to 4
the loop stops once count reaches 5'''

#Monitoring Fuel level
fuel_level = 10.0 # liters
threshold = 2.0

while fuel_level > threshold:
    print(f"Current fuel : {fuel_level} L")
    #simulate fuel consumption
    fuel_level -= 0.5

print("Low fuel alret! fuel below threshold")
# As long as fuel_level is greater than 2.0, keep printing and decrementing
# Once it drops to 2.0 or less, exit the loop and issue an alert
#Checking Engine Temperature in a HIL simulation
#Scenario: During a HIL test, you might loop until the engine temperature stabilizes / maximum time is reached.
engine_temp = 70.0
max_temp = 90.0
time_elapsed = 0

while engine_temp < max_temp and time_elapsed < 10:
    print(f"Engine temperature: {engine_temp}c, time : {time_elapsed}s")
    engine_temp +=2.0 # Simulate temperature rise
    time_elapsed += 1 # 1 second per loop iteration
if engine_temp >= max_temp:
    print("Max engine temp reached")
else:
     print("loop ended temp reached")

#Breaking out early: break and continue
'''break
exits loop immediately , regardless of the conditoin.

Use case: if a certain error state occurs and you need to stop.

continue
skips the rest of the current loop iteration and moves on t othe next iteration
use case: if you detect a conditoin where you want to ignore the rest of the code in this iteratoin but keep looping the 
rest of the code in this iteration but keep looping

ex:

#simulated list of sensor data

sensor_data_list =[12,3,4,45,-1, 13]

index = 0 # track the position in the list

while true:
if index >= len sensor_data_list):
break # no more data to read

sensor_data = sensor_data_list[index]
index +=1

if sensor_data < 0:
print("Error invalid sensor data!")
break # stop the loop immeditely

if sensor_data < 10:
print("sensor reading too slow, ignoring..")
continue # skip the rest of the iteration

#Normal processing
print(f"processing sensor data: {sensor_data}")

FLOW:
if sensor_data < 0, we break the loop
if 0<= sensor_data < 10 , we skip the rest of the iteration but keep looping
otherwise, we process the data

'''
#Avoidng infinite loops
'''an infinite loop occurs if the condition never becomes false
(or you never break)
Always ensire something insde the loop chnages the condition, you have a break for an escepe.

ex(common mistake)

count = 0
while count < 5:
print(count)
#if we forget count +=1, count stays 0 forever -> infinite loop
(Correct)

count =0
while count < 5:
print(count)
count+=1 # eventually count >= 5 -> exit loop

#Combine while with other conditionals

you can add nested if checks inside a while loop:

speed = 0
 while speed < 80:
 speed +=10
 print(f"speed is now {speed}")
 if speed>= 60 and speed < 80:
 print("with in modeerate speed range")
 
 # each iteration increments speed by 10 , checks if it's in a certain rnge, and continues until speed is 80 or more
 '''
#for loop
# loop iterates over elements of any iterable (ex: list, tuple, string, range), one by one , performing  a block of code on each elements
#key points
# no numeric index (for(i = 0; i<10; i++)) by default in Python
# Basic Syntax:
'''
for item in iterable:
# code block using item
 
 Automotive ex:1
 
sensor_readings ={12.0, 13.4, 11.3, 12.4, 12.9] # ex: battery voltages in volts

for volatge in sensor _readings:
print(f"voltage reading: {voltage} v")

ex: iterates over each volatge in the list and prints it'''

# Checking Conditions inside a for loop
fault_codes =['p0123', 'u0456', 'b1230','p0231']
for code in fault_codes:
    if code == "p0231":
        print("no fault code stored")
    else:
        print("active fault code: {code} ")
# ex: for each code, checks if it's "p0231'(indicating no fault) or prints it as active.
'''
Using conditions with a for loop:
if/else inside a for:
evaluate each item, conditionally do something (ex: filter, transform, etc)

break:
stop the loop early if a certain condition is met.
continue:
skip to the next loop iteration if a condiiton is met.

ex: early stop with break

speeds = [50, 60, 70, 80, 90]
for speed in speeds:
print(f'overspeeding at {speed} km/h stopping loop.')
break # stops the loop as soon as a  speed over 120 s found
print(f"speed{speed} km/h is with in limit.")

ex: once a speed above 120 is found, it prints a warning and ends the loop'''

# ex: skipping items with continue
engine_rpms = [200, 800, 1500, 500, 2200, 3000]
for rpm in engine_rpms:
    if rpm<600:
        continue # skips processing if the RPM is below 600
    print(f"processing rpm: {rpm}")
# ex: if rpm is below 600, it skips the rest of that iteration.

#looping with range and conditions
'''range() allows you to generate a sequence of numbers. this is useful if you need index based iteration / numeric loop

# simulate checking 10 time intervals for sensor data

for i in range(10):
    print(f"Time interval{i} : reading sensor...")
    #possibly some condition inside
example:
Check each index's sensor reading:

sensor_readings = [12.1, 12.5, 11.8, 14.0, 15.2]

for i in range(len(sensor_readings):
if sensor_readings[i]< 12.0:
print(f"reading{i} -> {sensor_readings[i]} V is too low!")

ex: This approach  uses i to acess the list by index

output: reading 1-> 11.9v is too low!
'''
# Using the for .. else clause
'''
for loop can have an else block that executes only if the loop completes normally(i.e no break )
ex:
fault_codes =['P0123', 'U0456', 'b1230', 'p0231']
for code in fault_codes:
if code.startswith("P0"):
print(f"special code found : {code}")
break
else:
#this runs only if the loop did not break
print("no P0-type code found in the list.")

#If we never break(no code started with "PO"), then the else executes.
#If we break early, the else is skipped.

output:
special code found : P0123'''
# nested for loops with conditions
'''
you can nest for loops, but be mindful of complexity
ex: suppose we have multiple sensors(rows) each with multiple readings(columns):'''


sensor_data = [[ 12.1, 11.9, 12.0],[13.1, 13.5, 14.0]] # sensor 1 , 2 readings

for sensor_index, readings in enumerate(sensor_data):
    print(f"sensor{sensor_index +1 }:")
for reading in readings:
    if reading < 12.0:
        print(f" lwo reading detected: {reading}")
    else:
        print(f" NOrmal reading: {reading}")

#ex: two nested loops- one for each sensor, and an inner loop for each sensors's readings

'''Commoon Pitfalls
#Off by one errors:
when using range(), ensoure that start and stop values are correct afor your scenario.
# Modifying a list while iterating:
removing items from a list your'e looping over can cause unexpected results
# Infinite loops in other languages:
Not typical with pythons's for (since it's tied to an iterable),
but possible if you're using a while or custom iterator incorrectly

A for loop is crucial for iterating over sequence (like sensor readings , fault codes) in automtotive or any python context . By incorporating conditions(if , break, continue, for , .. else), you gain fine-grained control over how data is processed when iteration stops, and how certian values are handled.'''

    

