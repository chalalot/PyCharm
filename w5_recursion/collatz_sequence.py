a = int(input("enter number: "))

def collatz(n):
    max1 = 0
    if n == 1:
        return max1
    else:
        if n % 2 == 0:
            i = n / 2
        else:
            i = n * 3 + 1
        return max(n, collatz(i))

print(collatz(a))

'''
i.e 10: = 10/2 
'''