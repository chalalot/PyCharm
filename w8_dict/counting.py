def count_dict(str):
    dct = {}
    for i in str:
        count = str.count(i)
        dct[i] = count
    return dct

print(count_dict('dncoasvijewriuvsvdadjonsvfnajc'))