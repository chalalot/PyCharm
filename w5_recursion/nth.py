a = int(input("enter size: "))

def nth(n):
    if n == 1:
        return 1
    else:
        return (n-1) * 5 + nth(n - 1)

print(nth(a))