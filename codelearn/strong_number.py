def factorial(n):
    if n == 1 or n == 0:
        return n
    else:
        return n * factorial(n - 1)

while True:
    n = input("enter strong number: ")
    lst = list(n)
    sum = 0
    for i in lst:
        i = int(i)
        sum += factorial(i)
    if int(n) == sum:
        print("True")
    else:
        print('False')