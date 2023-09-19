'''
File: 5.7.py
File Created: 2023/09/19 08:22:42
Author: Aaon212 (aaron212cn@outlook.com)

Copyright 2023 Aaron212
'''

binStr = input("Input a binary string >>>")
decNum = 0

for i in range(len(binStr)):
    if binStr[i] == "1":
        decNum += 2 ** (len(binStr) - 1 - i)
        
print(decNum)