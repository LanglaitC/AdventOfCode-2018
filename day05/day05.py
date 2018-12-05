with open('input.txt') as f:
    var = list(f.read())

#var = list('dabAcCaCBAcCcaDA')

reactions = None
polymers = list('abcdefghijklmnopqrstuvwxyz'.upper())
init = var.copy()
# PART 1
# while reactions is None or reactions > 0:
#     reactions = 0
#     i = 0
#     while i < len(var) - 1:
#         if i + 1 < len(var) and var[i].capitalize() == var[i + 1].capitalize() and var[i] != var[i + 1]:
#             del var[i]
#             del var[i]
#             reactions += 1
#         i += 1

# Remove one because of \n
# print(len(var))

# PART 2

res = {}
for each in polymers:
    print(each)
    reactions = None
    var = init.copy()
    i = 0
    while i < len(var):
        if var[i].capitalize() == each:
            del var[i]
            i -= 1
        i += 1
    while reactions is None or reactions > 0:
        reactions = 0
        i = 0
        while i < len(var):
            if i + 1 < len(var) and var[i].capitalize() == var[i + 1].capitalize() and var[i] != var[i + 1]:
                del var[i]
                del var[i]
                reactions += 1
            i += 1
    res[each] = len(var)

# Remove one from shortest because of \n
res = sorted(res.items(), key=lambda x: x[1])
print(res)