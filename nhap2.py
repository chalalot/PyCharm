def square(n):
    position = 0
    num = n
    count = 1
    for j in range(n*2-1):
        if 0 < j < n:
            position += 1
        elif n-1 < j < n*2-1:
            position -= 1

        for i in range(n*2-1):
            print(num, end='')
            if 0 < count+1 < position+1:
                num -= 1
            elif (n*2-1-position-1) < count+1 < n*2-1:
                num += 1
            count += 1
        print()
        count = 0

square(4)