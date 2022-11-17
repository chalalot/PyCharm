# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2022C
# Assignment: 1
# Author: Tran Tuan Trung
# Created date: 19/11/2022
# Last modified date: 19/11/2022

num = input("Enter an integer number: ")

def reverse(n):
    if int(n) > 0:
        new_num = n[::-1] #reverse the number by step negative
        return new_num
    else:
        new_num = n[::-1]

        return "-",new_num

print(reverse(num))