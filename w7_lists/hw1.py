'''
the program takes input as comma-sequenced numbers
and square them
'''
lst = input("enter number: ")


def input_(ls):
    '''
    take input of user as numbers-comma sequence
    :return:
    '''
    ls = list(ls) #break the string out
    for i in ls:
        if i == ',': #remove the excess comma
            ls.remove(i)
    ls = list(map(int, ls))
    return ls


def square(ls):
    new_lst = []
    for i in ls:
        if i % 2 != 0:
            new_lst.append(i**2)
    return new_lst


lst = input_(lst)
print(lst)
print(square(lst))