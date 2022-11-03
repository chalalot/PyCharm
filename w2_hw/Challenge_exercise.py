def reach_one(n):
    lst = []
    while True:
        if n > 1:
            if n % 2 == 0:
                n = n / 2
                lst.append(n)
            else:
                n = n * 3 + 1
                lst.append(n)

        elif n == 1:
            break
    return lst

new_lst = []
for i in range (2, 101):
    new_lst.append(max(reach_one(i)))

print(max(new_lst))
