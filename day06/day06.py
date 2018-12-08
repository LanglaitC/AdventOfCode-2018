from pprint import pprint
import json

with open('input.json') as f:
    coord = json.load(f)["coord"]

maxX = 0
maxY = 0

indexes = {}
for key,each in enumerate(coord):
    indexes[key] = coord[key]
    maxX = coord[key]['x'] if coord[key]['x'] > maxX else maxX
    maxY = coord[key]['y'] if coord[key]['y'] > maxY else maxY

iteration = 0
grid = [['#' for x in range(maxX + 1)] for y in range(maxY + 1)]
print(len(grid[0]))
print(len(grid))
print(maxX, maxY)
for each in indexes:
    print(indexes[each]['y'])
    grid[indexes[each]['y']][indexes[each]['x']] = {'key': each, 'iter': iteration}