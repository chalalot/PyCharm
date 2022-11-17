a = int(input("enter number: "))

def collatz(n):
    max = n
    if n == 1:
        return max
    else:
        if n % 2 == 0:
            return (collatz(n/2))
        else:
            if n*3 + 1 > max:
                max = n*3+1
            return max

print(collatz(a))

'''
i.e 10: = 10/2 
'''