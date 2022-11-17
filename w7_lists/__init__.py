# import random
#
# a = [1,2,3]
# b = a[:]
#
# print(a == b)
# print(a is b)
#
# b[0] = 5
# print(a)
# print(b)
#
# result = []
# for i in range (1001):
#     n = random.randrange(1001)
#     result.append(n)
#
# print(result)

s = "python rocks"
idx = 1
while idx < len(s):
    print(s[idx])
    idx = idx + 2