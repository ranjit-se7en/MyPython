import json
import sys
import os
from datetime import datetime
import re



#C:\Users\rpradhan\assignment.json

# filename="assignment.json"
# #data=dict()
# #filename=sys.argv[1]
# #numberofdays=sys.argv[2]
# currentdate=datetime.today().strftime('%Y-%m-%d')
#
# print("Current date is" + currentdate)
#
# with open (filename, 'r') as f:
#     for line in f:
#         #print(f.readline())
#         if re.search('creationTimestamp', line):
#             #print(line)
#             x=re.split("T", line)
#             y=x[1].split('": "')
#             z=y[1]
#             print( currentdate - z + "days")
#
# # for i in z:
# #     if


import json
json_obj =  '{ "Name":"David", "Class":"I", "Age":6 }'
python_obj = json.loads(json_obj)
print("\nJSON data:")
print(python_obj)
print("\nName: ",python_obj["Name"])
print("Class: ",python_obj["Class"])
print("Age: ",python_obj["Age"])

# a Python object (dict):
python_obj = {
  "name": "David",
  "class":"I",
  "age": 6
}
print(type(python_obj))
# convert into JSON:
j_data = json.dumps(python_obj)

# result is a JSON string:
print(j_data)

# with open ("assignment.json", "r") as file:
#     data=json.load(file)
#     #print(data)
#     dict(data)
#     print(data)
#     print(type(data))



str = "pynative"
print (str[1:3])
print(str[0])


# var= "James Bond"
# print(var[2::-1])

var = "James" * 2  * 3
print(var)


x = 36 / 4 * (3 +  2) * 4 + 2
print(x)

# sampleSet = {"Jodi", "Eric", "Garry"}
# sampleSet.add(1, "Vicki")
# print(sampleSet)


listOne = [20, 40, 60, 80]
listTwo = [20, 40, 60, 80]

print(listOne == listTwo)
print(listOne is listTwo)

print(bool(0), bool(3.14159), bool(-3), bool(1.0+1j))

print(type({}))


