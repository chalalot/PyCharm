def square_of_even(ls):
    '''
    produce a list of square of even numbers in the input list
    :return:
    '''
    new_lst = []
    for i in ls:
        if i % 2 == 0:
            new_lst.append(i**2)
    return new_lst
lst = [1,2,3,4,5,6,7,8,9,10]

print(square_of_even(lst))

