'''
this takes the square of numbers from 1 to 100
and prints out the last 5
'''

ls = []
for i in range (101):
    ls.append(i**2)

print(ls[-5:]) # start -5 till end, step = 1