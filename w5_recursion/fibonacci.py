def rabbits(n):
    '''
    this function will calculate the number of rabbits
    after the input 'n' month
    :param n:
    :return:
    '''
    while n >= 2:
        return (rabbits(n-2) + rabbits(n - 1))
    else:
        return n

''' if n = 5 then r(3)+r(4)...'''

print(rabbits(8))