import string

n = input("Enter password: ")

a = list(string.ascii_letters)
A = list(string.ascii_uppercase)
num = list(string.digits)
sign = ['#','$', '@']
boolean = False
for i in n:
    if i in a:
        boolean = True
    if i in A:
        boolean = True
    if i in num:
        boolean = True
    if i in sign:
        boolean = True
    else:
        print('invalid password')