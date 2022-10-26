n = int(input("enter your number "))
lst = []
for i in range (1, n + 1):
    if n % i == 0:
        lst.append(i)

if lst == [1, n]:
    print("this number is prime")
else:
    print(lst)