# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2022C
# Assignment: 1
# Author: Tran Tuan Trung
# Created date: 19/11/2022
# Last modified date: 19/11/2022

def is_divisible_by_7(n): #define the function
    for i in range (n, 4 * n): #call a loop that runs from n(inclusive) to 4n(exclusive)
        if i % 7 == 0: #condition
            print(int(i))


num = int(input("Enter an interger number: ")) #ask for input
while True:
    if num > 2:
        print(is_divisible_by_7(num)) #print the answer using num as a parameter
        break
    else:
        print("invalid input, please enter an interger that is greater than 2.") #description for invalid input
