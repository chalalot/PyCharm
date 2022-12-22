# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2022C
# Assignment: 1
# Author: Tran Tuan Trung
# Created date: 17/12/2022
# Last modified date: 17/12/2022

given_str = input(" Enter a string: ")

def character_count(n):
    '''
    return the number of letters, digits and symbols included in the given string
    :param n:
    :return: the total number of each character types
    '''
    al = 0
    dgt = 0
    sym = 0
    for i in n:
        if i.isalpha():
            al += 1
        elif i.isdigit():
            dgt += 1
        else:
            sym += 1

    print("Letters:", al)
    print("Digits:", dgt)
    print("Symbols:", sym)

character_count(given_str)