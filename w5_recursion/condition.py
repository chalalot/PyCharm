grade = float(input("Enter your final mark "))

while grade >= 0 and grade <= 100:
    if grade >= 80:
        print("HD")
    elif grade >= 70 and grade < 80:
        print("DI")
    elif grade >= 60 and grade < 70:
        print("CR")
    else:
        print("NN")
    break