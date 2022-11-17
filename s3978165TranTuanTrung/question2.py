# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2022C
# Assignment: 1
# Author: Tran Tuan Trung
# Created date: 19/11/2022
# Last modified date: 19/11/2022

def factorial(n): #declare function
    if n == 1 or n == 0: # the factorial of 0 and 1 is 1
        return 1
    else:
        return n * factorial(n - 1) #if n still larger than 1, the factorial equals to n * (n-1)!
                                    #calls the function itself until n = 1

while True: #a loop to ask for input
    num = int(input("Enter a number: "))
    if num >= 0:#when it is satisfied, break the loop
        break
    else: #while not satisfied, ask for input again
        print("Factorial does not exist for negative number")

print("The factorial of", num, "is", factorial(num))