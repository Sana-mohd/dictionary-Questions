dic={
    "ball":"red",
    "bat":4,
    "wickets":8,
    "ball":"green",
    "bat":3
    }
#as in dic no duplicates are allowed so by just printing dic we will get no duplicates
res = {}
for key, val in dic.items():
    if val not in res:
        res[key] = val
print(res)