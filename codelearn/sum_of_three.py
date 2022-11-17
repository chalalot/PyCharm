def sum_of_three(n):
    '''
    this function checks if the input number
    could be break down into sum of 3 consecutive numbers or not
    :param n:
    :return:
    '''
    lst = []
    if n % 3 == 0:
        for i in range (n//3 + 1):
            if (i - 1) + i + (i + 1) == n:
                lst.append(i)
        if len(lst) == 1:
            return 'true'
        else:
            return 'false'
    else:
        return 'false'

print(sum_of_three(33))