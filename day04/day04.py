import json
import re
from pprint import pprint

with open('input.json') as f:
    var = json.load(f)["var"]


var = sorted(var, key=lambda x: x['time'])
    

data = {}
currentId = None
state = None
for each in var:
    if isinstance(each['action'], int):
        currentId = each['action']
        if currentId not in data:
            data[currentId] = []
        state = 1
    elif each['action'] == 'wake' and state == 0:
        state = 1
        currentWake = int(each['time'][14:16])
        data[currentId].append([currentSleep , currentWake])
    elif each['action'] == 'sleep' and state == 1:
        state = 0
        currentSleep = int(each['time'][14:16])

res = {}
for each in data:
    res[each] = {'result':0}
    for entry in data[each]:
        res[each]['result'] += entry[1] - entry[0] 
        for number in range(entry[0], entry[1]):
            if number in res[each]:
                res[each][number] += 1
            else:
                res[each][number] = 1

maxRes = 0
maxKey = None
for each in res:
    if res[each]['result'] > maxRes:
        maxRes= res[each]['result']
        maxKey = each

print(maxKey)
#pprint(res[maxKey])

maxRes = 0
maxKey = None
guard = None
for each in res:
    for minute in res[each]:
        if minute != 'result':
            if res[each][minute] > maxRes:
                maxRes =  res[each][minute]
                maxKey = minute
                guard = each

print maxKey, guard
