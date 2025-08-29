#Lists an ordered, changeable(mutuable), collection of items
# []
'''
my_list = [item1,item2,item3]
Common OPerations:
1. Indexing & Slicing:
---------------------
values = [10,20,40,34,56,78,86,54,43]
first_item = values[0]  #10-> first element (index 0)
last_item = values[-1]  # 50 -> last element (negative index)
slice_mid = values[1:8]  # [20,...54] ->items at index 1-7(8 is excluded)

print("First item:", first_item)
print("Last item:", last_item)
print("Middle item:", slice_mid)

2. Appending and Inserting
-----------------------------------

values = [10,20,30,40,50]
values.append(60)  # adds 60 at the end -> [10, 20, 30, 40, 50]
values.insert(2,25)  #Inserts 25 at index 2 -> [10, 20, 30, 40, 50]
print(values)

3. Removing items
--------------------------------

values = [10,20,30,40,50,60]
values.remove(30) #Removes the first occurence of 30
popped_value = values.pop() # Removes and returns the last item 60
print(values)
print("popped:", popped_value) #popped:60

4. Iterating
---------------------------------

values = [10,20,30,40,50,60]
for v in values:
    print(v)

5. Length and Membership
----------------------------------

values = [10,20,30,40,50,60]
length = len(values) #Gets the number of elements ion the list
if 43 in values:
    print("Found 40 in the list")
else:
    print("Not found")

Automotive ex:
----------------------------------

Scenario: storing sensor reading / speeds in a ist

speed_ratings = [50, 60, 70, 80]
speed_ratings.append(90)
print(speed_ratings)
# You can keep adding speeds as the vehicle accelerates
'''
from PyCantoools.database.can.c_source import PACK_HELPER_RIGHT_SHIFT_FMT

# Dictionaries
# Key-Value pairs,{} with key: value pairs
'''
my_dict ={"key1": value1, "key2" : value2}
Common Operations:
-----------------------------
1. Acessing and updating values
----------------
'''
dtc_codes = {"P0123": "Throttle Pos Sensor", "U0456": "Invalid data"}
code_desc = dtc_codes["P0123"]#"throttle Pos Sensor
dtc_codes["P0123"] = "TPS Fault" #Update value
print(dtc_codes)
''''
2. Adding New pair_s
---------------
'''
dtc_codes["B1482"] = "Brake Switch Circuit"
print(dtc_codes) #o/p:- {'P0123': 'TPS Fault', 'U0456': 'Invalid data', 'B1482': 'Brake Switch Circuit'}
'''
3. Checking Membership
'''
if "P0123" in dtc_codes:
    print("code P0123 found")
'''
4. Removing items

'''
removed_value = dtc_codes.pop("U0456") #Removes key "UO456" and returns its value
print(removed_value) # o/p: Invalid data

del dtc_codes["P0123"] # removes key "P0123"
print(dtc_codes)  #o/p:-  {'B1482': 'Brake Switch Circuit'}

'''
5.Iterating Over Keys/Values

'''
for code, desc in dtc_codes.items():
    print(code, "->", desc) #B1482 -> Brake Switch Circuit

#Automotive Example:
'''----------
Scenario: Mapping DTC to descriptions.
'''

dtc_codes = {
    "P0123": "Throttle Pos Sensor",
    "U0456": "Invalid data",
    "B1482": "Brake Switch Circuit",
    "P0122" : "throttle Position Sensor a Circuite Low",
    "P0125": "throttle Position Sensor a Circuite High"}

if "P0123" in dtc_codes:
    print("code P0123 found")
else:
    print("code P0123 not found") #code P0123 found

