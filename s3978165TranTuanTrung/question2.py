# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2022C
# Assignment: 1
# Author: Tran Tuan Trung
# Created date: 17/12/2022
# Last modified date: 17/12/2022

def filter_vowels(strng):
    '''
    filter out words that don't start with vowels
    the sequence is separated by commas
    :param str
    :return: string
    '''
    vowels = ['a', 'e', 'i', 'o', 'u']
    string = strng.split(',')
    word_list = []
    filter = []
    for i in string:
        word_list.append(str(i))
    for word in word_list:
        if word[0].lower() not in vowels:
            filter.append(word)
    return filter

user = str(input('Enter the words separated by comma: '))
print(filter_vowels(user))