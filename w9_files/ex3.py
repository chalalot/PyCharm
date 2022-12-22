name = str(input("Enter your file name: "))
num = 1
with open(name, 'r') as input_file:
    lines = input_file.readlines()
with open('new_' + name, 'w+') as file:
    for l in lines:
        file.write(str(num))
        file.write(l)
        num += 1

file.close()