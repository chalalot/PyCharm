import string

'''a = int(input("table size: "))
b = int(input("table size: "))
print(format('x',">5"),end=' ')
for i in range (a + 1):
    print(format(i,">5"), end=' ')
print()
for i in range (b + 1):
    print(format(i,">5"), end=' ')
    for j in range (a + 1):
        print(format(i*j,">5"), end=' ')
    print()
'''

def digit(n):
     return len(str(n))

def reverse(n):
    return n[::-1]

def palindrome(n):
    n=n.replace(' ','')
    if n[::-1] == n:
        return True
    return False

def letter(n, a):
    n = n.replace(a,'')
    return n

