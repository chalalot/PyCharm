p = int(input("enter your initial amount: "))
t = int(input("enter your time (years): "))
n = 12
r = 0.08

def final_amount():
    A = p*(1+r/n)**(n*t)
    return A

print("after", t, "years, you will get", final_amount())