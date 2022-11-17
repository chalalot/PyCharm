def filter_even(ls):
    '''
    this funtion filtered all the even elements in a list
    :return:
    '''
    for i in ls:
        if i % 2 != 0:
            ls.remove(i)
    return ls

lst = [1,2,3,4,5,6,7,8,9]
print(filter_even(lst))
