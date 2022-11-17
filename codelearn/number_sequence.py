def sequence(a,b):
    '''
    find numbers with ascending elements
    :param a:
    :param b:
    :return:
    '''
    ls = []
    for i in range (a, b+1):
        lst = []
        lst = list(str(i))
        lst = [int(m) for m in lst]
        n = 0
        num = []
        for j in lst:
            if j+1 == lst[n]:
                num.append(j)
                n += 1
        ls.append(num)
    return ls

print(sequence(10,30))