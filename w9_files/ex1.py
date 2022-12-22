message = input("Enter message: ")

with open('message.txt', 'w') as filename:
    for i in range (100):
        filename.write(message)
        filename.write('\n')

filename.close()