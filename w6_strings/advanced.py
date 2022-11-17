import string
all = string.ascii_letters
text = str(input("enter your text: "))
cipher = []
dict = {}

for i in range (len(string.ascii_letters)):
    dict[string.ascii_letters[i]] = string.ascii_letters[i - 36]

for char in text:
    if char in all:
        temp = dict[char]
        cipher.append(temp)
    else:
        temp = char
        cipher.append(temp)
cipher = "".join(cipher)
print("encrypted: ", cipher)

dict1 = {}
decrypt = []
for i in range (len(string.ascii_letters)):
    dict[string.ascii_letters[i]] = string.ascii_letters[i - 36]


def decrypt():
    for char in cipher:
        if char in all:
            temp = dict1[char]
            decrypt.append(temp)
        else:
            temp = char
            decrypt.append(temp)
