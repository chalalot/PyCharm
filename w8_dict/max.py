inv = {'a': 1, 'b':2, 'c':3, 'd':4}

keys = list(inv.keys())
values = list(inv.values())

print(keys[values.index(max(values))])