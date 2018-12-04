import json
import re
from pprint import pprint

with open('input.json') as f:
    var = json.load(f)["var"]

data = {}
currentId = None
for each in var:
    currentDate = re.search(r'[0-9]{4}-[0-9]{2}-[0-9]{2}', each['time']).group()
    if isinstance(each['action'], int):
        currentId = each['action']
        data[currentId]['sleepTime'] = 0
        if currentId not in data:
            data[currentId] = {}
    elif each['action'] == 'wake':
        wakeTime = re.search(r'[0-9]{2}:[0-9]{2}', each['time']).group()
        if currentDate in data[currentId]:
            data[currentId][currentDate]['wake'] = wakeTime
        else:
            data[currentId][currentDate] = {'wake' : wakeTime}
    elif each['action'] == 'sleep':
        lastSleep = re.search(r'[0-9]{2}:[0-9]{2}', each['time']).group()
        if currentDate in data[currentId]:
            data[currentId][currentDate]['sleep'] = lastSleep
        else:
            data[currentId][currentDate] = {'sleep' : lastSleep}

for each in data:
    print(data[each])
        
pprint(data[2689])