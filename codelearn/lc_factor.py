def solve(a,b):
    '''
    the function returns the number of number which have odd factor in range a to b
    :param a:
    :param b:
    :return:
    '''
    count = 0 # factor count
    answer = 0
    for i in range(a, b + 1): # examining i from a to b
        for j in range (1, i + 1):
            if i % j == 0:
                count += 1 #counting factor
        if count % 2 == 1: #done counting factor, move to answer adding
                answer += 1 #adding to the answer
        count = 0
    return answer
print(solve(1,10))