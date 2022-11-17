a = int(input("enter the harmonic length: "))

def harmonics(n):
    if n == 0 or n == 1:
        return 1
    else:
        return  1/n + harmonics(n-1)


print("the answer is ", harmonics(a))
'''
n = 5 => 1/5 + 1/4 + 1/3 + 1/2 + 1/1
= 1/5 + r(4)
= 1/5 + 1/4 + r(3)
= .....+ r(1) 
'''