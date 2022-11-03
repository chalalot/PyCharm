a = str(input("enter your starting day: "))
b = int(input("enter your vacation's length: "))
end = 0

if a + b > 6:
    end = -1 + (b - (6 - a))

print(end)