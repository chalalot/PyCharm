n = int(input("Enter size: "))

def draw_triangle(n):
    '''
    the function draws 2 triangles using * and ~ symbol
    :param n:
    :return:
    '''
    a = n #store the size as another variable
    for i in range (1, n + 1): #n rows
        for j in range (1, a): #n columns
            print('~', end='')
        a -= 1 #after printing the ~, decrease the size for next row
        for k in range (i): #the higher the row, the more * is printed
            print('*', end='')
        print()
draw_triangle(n)