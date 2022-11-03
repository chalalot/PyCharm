running = True
lst = []
while running:
    n = input("enter your number: ")
    if n != 's':
        lst.append(n)
    else:
        break


def find_min():
    minV = lst[0]
    for i in lst:
        if i < minV:
            minV = i

    return minV


def find_max():
    maxV = lst[0]
    for i in lst:
        if i > maxV:
            maxV = i
    return maxV


def find_average():
    sum = 0
    for i in lst:
        sum += int(i)
    avg = int(sum) / int(len(lst))

    return avg


print(lst)
print(find_min())
print(find_max())
print(find_average())

