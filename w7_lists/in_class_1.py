print("press q to quit")
lst = []
while True:
    n = input("Enter your element: ")
    if n == 'q':
        break
    else:
        lst.append(n)

lst.sort()
print(lst)