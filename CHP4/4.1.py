'''
File: 4.1.py
File Created: 2023/09/18 22:50:43
Author: Aaon212 (aaron212cn@outlook.com)

Copyright 2023 Aaron212
'''

inputString = input("Enter a string >>>")
letterCount, digitCount, spaceCount, otherCount = 0,0,0,0
for i in range(len(inputString)):
    i = ord(inputString[i])
    if 65<=i<=90 or 97<=i<=122:
        letterCount+=1
    elif 48<=i<=57 :
        digitCount+=1
    elif i == 32 :
        spaceCount+=1
    else:
        otherCount+=1

print(f"letterCount: {letterCount}, digitCount: {digitCount}, spaceCount: {spaceCount}, otherCount: {otherCount}")