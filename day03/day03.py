import json

with open('input.json') as f:
    var = json.load(f)["var"]

tissue =  [['.' for x in range(1000)] for y in range(1000)]
print(len(tissue[0]))

hashed = {}
for each in var:
    for y in range(each['dim'][0], each['dim'][0] + each['size'][0]):
        for x in range(each['dim'][1], each['dim'][1] + each['size'][1]):
            hashed[each['id']] = {'required': each['size'][0] * each['size'][1], 'done': 0}
            if (tissue[y][x] == "."):
                tissue[y][x] = each['id']
            else:
                tissue[y][x] = '#'

res = 0
for y in range(1000):
    for x in range(1000):
        if (tissue[y][x] in hashed):
            hashed[tissue[y][x]]['done'] += 1
        if (tissue[y][x] == "#"):
            res += 1

for each in hashed:
    if hashed[each]['required'] == hashed[each]['done']:
        print(each)
print(res)
 