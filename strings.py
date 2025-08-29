# it is a sequence of unicode characters
#""" """ or ''' '''
#immutable, once created , they cannot be changed
#any operatoin that seems to "modify" a string actually creates a new string

# Automotive example
'''vin_number = "1HCM823487T6A000345" #vEHICLE
Identitifcation Numbber
 ecu_Sfotware ='1234-AB'
1. Single Quotes
part_number ='1234-AB'
2. Multi Quotes
part_number ="V8 Egine"

3.Triple Quotes(for multi-line / docstrings):
car_description = """ This is a sport casr
"""
4. Escap Sequences(eg., \n for new line, \" for oduble quote inside a string

message ="Engine \"Overheated\"Alert!"
print(message) #Engine"Overheated"Alert!

String Indexing and Slicing
----------------------------
String are indexed from 0 up to len(string)-1

Index: Acess a single character

Slice: Extract a substring using [Start:Stop:Step]

Indexing Ex:
----------------
model ="Civic"

print(model[0])#'C'
print(model[1])#'i'
print(model[-1])#'c'(Last charcter)

Slicing Ex:
---------------

vin = "1HGCM8263A004352"

print(vin[0:3]) #'1HG'(CHARACTERS 0,1,2)
print(vin[3:8]) #'CM826' (characters 3...7)
print(vin[-4:]) # '4352' (last four characters)

Default: vin[:5] -> from start to index 4, vin[5:] -> index 5 to end

Common Sting Operations:
-------------------------

1. Concatenation:

make = "Honda"
model = "Civic"
full_Car_name = make + " " + model
print(full_car_name) # 'Honda Civic'

2. Repetition
separator = "-"
line = separator * 10
print(line) #"---------"

#String Methods
len()
message = "Engine Overheated!"
print(len(message))  # Returns the no of characters in the string

Changing Case:
part_number = 'ab-1234'
print(part_number.upper()) #AB-1234
print(part_number.lower()) #ab-1234

strip(), rstrip(), lstrip
-------------
.Removes whitespace(or specified chars) from ends

ecu_line = "ECM-EngineControlModule"
clean_ecu = ecu_line.strip()
print(clean_ecu) # "ECM-EngineControlModule"

split() & join()
-----------------
split() breaks a string in to a list
join() joins list elements into a single string

data_line = "Engine, 120, Overheated"
parts = data_line.split(",")
print(parts) #o/p; ['Engine', ' 120', ' Overheated']
joined_line = ";".join(parts)
print(joined_line)

Replace()
-------------

warning_message = "Engine Overheated.Overheated condition critical!"
updated_message= warning_message.replace("Overheated", "HOT")
print(updated_message) #o/p:- Engine HOT.HOT condition critical!

find(), index()
----------------
search for substring occurences
find() return -1 if not found
inedx() raises an error if not found

ex:
dtc_report = "Active DTC:P0123,P04555"
pos = dtc_report.find("P0123")
print(pos) #11 (index where "P0123" is starts)

#Formatting strings
1.F-string

engine_speed = 2500
info = f"EngineSpeed is {engine_speed} km/h"
print(info)

format() Method
-------------------

temperature = 95.5

msg = "Engine temperature: {:.1f}celsius".format(temperature)
print(msg) #o/p :- Engine temperature: 95.5celsius

Old-Style % Formating
----------------

Voltage = 12.8
print("Battery voltage =%.2f V" % Voltage) #Battery voltage =12.80 V
.less common nowaddays , but still seen in leagacy code

Automotive-Focused String Ex:
1. Constructing a VIN Description:
----------------------------------------------
vin = "1HGCM82633A00452"
make = "Honda"
model = "Civic"
description = f"Vehicle: {make} {model}, VIN: {vin}"
print(description) # o/p:- Vehicle: Honda Civic, VIN: 1HGCM82633A00452

2. Parsing a CSV log line(ex: from a sensor log):
--------------------------------------------------------
log_line = "TIME=10.00,SPEED = 100,ENGINE_TEMO =90.5"
items = log_line.split(",")
print(items)  #o/p:- ['TIME=10.00', 'SPEED = 100', 'ENGINE_TEMO =90.5']
for item in items:
    key, value= item.split("=")
    print(f"{key} -> {value}")

3. Replacing fault codes:
-----------------------------

dtc_report = "P0123 active, P0456 pending"
fixed_report = dtc_report.replace("P0123", "throttle Pos Sensor")
print(fixed_report) #o/p:- throttle Pos Sensor active, P0456 pending

#Common mistake to avoid

1.Off-by-One Errors in slicing:
remember that slicing is up to but not icluding the stop index

2. Forgetting Immutability:
doing somethins like some_String[0] = 'A' is not allowed.You must craete new string

3. Mixing data types with out conversion:

ex: print("speed:" + 120) -> typeError, Instead, convert the number to string: "Speed:" +str(120) or use f-strings
'''




