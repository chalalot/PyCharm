n = input("enter binary: ")

n = n.split(',')
lst = []
for i in n:
    num = 0
    a = 0
    for j in list(i):
        j = int(j)
        num += 2**a
        a += 1
    lst.append(num)
    num = 0

for k in lst:
    if k % 5 == 0:
        print(n[lst.index(k)])
