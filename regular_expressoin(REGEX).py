# Regular Expression are a sequence of characters that definea search pattern
#Usage in Python : Accessed via the built-in remodule
"""
Why in Automotive?

1. Parsing large diagnostic logs for specific error codes(ex: DTC like P0123)
2. Extracting sensor ID/CAN from textual data
3. Validating part numbers, vehicle IDs (VIN), or even firmware version strings

Basic Regex function in Python
--------
1.re.search(pattern, string): Finds the first match of pattern in string
2. re.findall(pattern, string): Returns a list of alll matches of pattern in string
3. re.match(pattern , string): Determines if the pattern matches at the start of the string
4. re.sub(pattern, repl, string): Replaces matches of pattern in string with repl

Common Regex MetaCharacters
1. .(dot):Matches any single character(except new line)
2. ^: Matches the start of a string
3. $: Matches the end of a string
4. *,+.?: Quantifiers for reptition
a.  *: zero or more occurrences
b. +: one o rmore occurences
c. ?:zero or one ocurence

5. {}:character classes (ex: [A-F0-9] matches a single hex character

6. (): Grouping, capturing subpatterns

#Automotive Use Cases
Extracting DTCs from Logs

Scenario
. You have alog containing lines like:

yaml
2025-01-03 12:00:00 -  ERROR - Detected DTC P0123
2025-01-03 12:05:00 - INFO -DTC U0456 cleared
2025-01-03 12:10:00 -ERROR -Fault code B1482 active

Regex Pattern

r"(P|U|B)/d{4}":
Explanation
1. (P|U|B): DTCs often start with P,U, or B.

2. (/d{4}) : Followed byexactly 4 digits

#python ex:
import re
log_data = "
2025-01-03 12:00:00 -ERROR - Detected DTC P0123
2025-01-03 12:05:00 - INFO -DTC U0456 cleared
2025-01-03 12:10:00 - ERROR - Fault code B1482 active 
"

pattern = r"(P|U|B)/d{4}"
dtcs = re.findall(pattern, log_data)
print("DTCs found:", dtcs)

NOte: if you want to capture the entire code(P0123) RATHER THAN ONLY THE LETTER(P) from the capturing group,
modify the pattern to r"(?:P|U|B)/d{4} or r"[PUB]/d{4}".

Validating PART Numbers
-------------------------
Scenario:
1. Suppose a valid part number format
----------

# 4 digits then a dash, then 2 upper case letters ex: 1234-AB

Regex Pattern
-------------

r"^/d{4}-[A-Z]{2}$"

^ start of string
/d{4} exactly 4 digits
-a dash
[A-Z]{2} exactly 2 uppercase letters
$ end ofstring


import re
# part number to validate
part_number = '1234-AB'

# Regular expression pattern to match a valid part number(4 digit followed by a dash and 2 uppercase latters)
pattern = r"^/d{4}-[A-Z]{2}$"

#Match the part number aganist the pattern
match = re.match(pattern, part_number)

#Check if the match is found
if match:
    print(f"{part_number} is a valid part number")
else:
    print(f"{part_number} is invalid")
# out put: 1234-AB is invalid
"""
#Parsing CAN Messages from Text
#Scenario
'''
you have a texttual log that includes lines iwth CAN ID's and data:
les 
[CAN]ID : 0X123 DATA:01 02 03 04
[CAN]ID :0X200 DATA:FF EE DD CC

Regex pattern
ex: r"ID:0X[A-Fa-FO-9]/S +DATA:([A-Fa-F0-0/s]+)"
 ID:0X- literal text
 ([A-Fa-F0-9]+) : CAPTURE hex xharacters for ID
 /s+- one or more white spaces characters
 DATA: LITER TEXT
 ([A-Fa-f0-9/s]+): capture the hex data bytes plus whitespaces
 
 #Python Ex:
 #sample CAN log data
import re

log = "
[CAN] ID:0X123 DATA:01 02 03 04
[CAN] ID: 0X200 DATA: FF EE DD CC
"

# Match: optional space after "ID:", 0x/0X, hex ID, then DATA and hex bytes
pattern = r"ID:\s*0[xX]([0-9A-Fa-f]+)\s+DATA:\s*((?:[0-9A-Fa-f]{2}\s*)+)"

matches = re.findall(pattern, log)

for can_id, can_data in matches:
    # split into clean byte list (['01','02',...])
    bytes_list = can_data.strip().split()
    print(f"CAN ID: 0x{can_id.upper()}, Data Bytes: {bytes_list}")

# For sanity, also show how many matches were found
print("Total frames found:", len(matches))
[o/p : CAN ID: 0x123, Data Bytes: ['01', '02', '03', '04']
CAN ID: 0x200, Data Bytes: ['FF', 'EE', 'DD', 'CC']

#Useful Regex Methods for Automotive

1. re.split(pattern, string): splitting large logs/ sensor data lines.
2. Named groups: 
pattern = r"(?P<dtc_type>[PUB])(?P<code>\d{4})"
3. Flags (re.IGNORECAE, re.MULTILINE, etc) to handle case-sensitive mathes or multiline logs.

 '''
help(print)
