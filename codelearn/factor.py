def is_prime(n):
    factor = []
    for i in range (1, n + 1):
        if n % i == 0:
            factor.append(i)
    if len(factor) == 2:
        return True
    else:
        return False

while True:
    '''
    list out prime factors of a number
    '''
    n = int(input("enter your number: "))

    prime_lst = []
    for i in range (2, n + 1):
        if is_prime(i):
            prime_lst.append(i)

    while n != 1:
        for i in prime_lst:
            if n % i == 0:
                a = i
        n = n / a
        print(a, end=' ')
    print()