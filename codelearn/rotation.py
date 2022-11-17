def rotation(lst, d):
    n = len(lst)
    m = 0
    org_lst = lst
    for i in range (d): #rotate d times
        lst = lst[-(n - 1):]   #slice the list except for the first one
        lst.append(org_lst[m])
        m += 1
    print(lst)
    return lst[0]

print(rotation([1,2,3,4,5],3))