inv = {'a':1, 'b':2, 'c':3, 'd':4}

key_list = list(inv.keys())
val_list = list(inv.values())

for i in inv.values():
    if i > 2:
        print(key_list[val_list.index(i)])