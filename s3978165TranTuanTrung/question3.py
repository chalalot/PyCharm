# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2022C
# Assignment: 1
# Author: Tran Tuan Trung
# Created date: 17/12/2022
# Last modified date: 17/12/2022
def find_max(nums):
    '''
    seperate sequence of numbers and then find the maximum value and all their position
    :param nums: string
    :return: string
    '''
    nums = str(nums).split()

    for i in nums:
        if i == ' ':
            nums.remove(i)

    num_list = [float(i) for i in nums]
    max_num = max(num_list)

    if num_list.count(max_num) == 1:
        return 'The maximum value is ' + str(max_num) + ' at position ' + str(num_list.index(max_num))
    else:
        #get all the position of the max number
        pos = [str(i) for i, x in enumerate(num_list) if x == max_num]
        #turn list into string
        pos = ','.join(pos)
        return 'The maximum value is ' + str(max_num) + ' at position ' + pos


sequence = input('Enter sequence: ')
print(find_max(sequence))