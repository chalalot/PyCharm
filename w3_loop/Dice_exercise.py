# Trung-s3978165
# Roll the dice 5 times

import random

def Rolling_Dice():
    lst = []    # Answer list
    for i in range (1, 6):  # Looping from 1 to 5 to do 5 times of rolling
        rand = random.randrange(1, 7)   # The dice has 6 faces
        lst.append(rand)    # Append the random value to answer
    return lst  # Return the answer

print(Rolling_Dice())   # Prints out the answer