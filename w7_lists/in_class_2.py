'''
this code prints out a table of multiplication
as table form
'''

rows = int(input("enter rows: "))
columns = int(input("enter columns: "))

count = 0
ls1 = []
ls2 = []
#make a big one that contains the number of rows lists
for j in range (rows):
    for i in range (columns):
        count += 1
        ls1.append(i * j)
        if count == columns:
            ls2.append(ls1)
            count = 0
            ls1 = []

print(*ls2,sep="\n")
print(ls1)


