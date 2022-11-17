def is_prime(n):
    factor = []
    for i in range (1, n + 1):
        if n % i == 0:
            factor.append(i)
    if len(factor) == 2:
        return n

n = int(input("Enter your number: "))
lst = []
for i in range (2,n):
    if is_prime(i):
        lst.append(i)
print(lst)
