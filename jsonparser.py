import json
import sys
import os
from datetime import datetime
import re



#C:\Users\rpradhan\assignment.json

filename="assignment.json"
#data=dict()
#filename=sys.argv[1]
#numberofdays=sys.argv[2]
currentdate=datetime.today().strftime('%Y-%m-%d')

print("Current date is" + currentdate)

with open (filename, 'r') as f:
    for line in f:
        #print(f.readline())
        if re.search('creationTimestamp', line):
            #print(line)
            x=re.split("T", line)
            y=x[1].split('": "')
            z=y[1]
            print( currentdate - z + "days")

# for i in z:
#     if


