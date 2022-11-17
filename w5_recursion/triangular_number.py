a = int(input("Enter size of triangle: "))

def tri_num(n):
    '''n = 4 => 4 + tr(3)
    = 4 + 3 + tr(2) ...'''
    if n == 1:
        return 1
    else:
        return n + tri_num(n - 1)

print(tri_num(a))