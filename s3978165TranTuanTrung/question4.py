# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2022C
# Assignment: 1
# Author: Tran Tuan Trung
# Created date: 17/12/2022
# Last modified date: 17/12/2022

num = int(input("Enter the number of students: "))
def ways_of_representative(a, b):
    '''
    the function calculates the possible ways when choosing
    b representative from a students
    :param a:
    :param b:
    :return: number of ways
    '''
    if b == 0 or b == a:# when the number of the number to choose is equal to the number pool or equal to 0
        return 1
    else: #use recursive to add up using the pascal formula
        return ways_of_representative(a-1, b) + ways_of_representative(a-1,b-1)
def total_ways(n):
    '''
    return the total of possible ways when choosing out 1 to num number of
    students each time
    :param n: number of student to choose from
    :return: total
    '''
    total = 0 #declare total number of ways
    for i in range (n): #loop from choosing from 1 to n number of student each time
        total += ways_of_representative(n, i) # adds up the ways for each time
    return total

print("There are",total_ways(num), 'way to to select a representative board from', num, 'students.')