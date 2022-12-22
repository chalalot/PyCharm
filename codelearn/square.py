import string
def square(size):
    isize = str(size)
    for i in range (1,size):
        size += 1
    for i in range (size):
        if i == 0 or i == size - 1:
            for j in range (size):
                print(isize,end='  ')
            print()
        else:
            print(size)


square(4)