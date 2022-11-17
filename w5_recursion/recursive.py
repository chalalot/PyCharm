def mult(a , b):
    if b == 1:
        return a
    else:
        return a + mult(a , b-1)
# 4 multiplied by 5
# 4 plus 4*4
# 4 plus (4 plus 4*3)
# 4 + (4 + ....
#unitil 4 + 4 .....+ 4
print(mult(4,5))