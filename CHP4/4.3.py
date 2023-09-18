'''
File: 4.3.py
File Created: 2023/09/18 23:05:44
Author: Aaon212 (aaron212cn@outlook.com)

Copyright 2023 Aaron212
'''

dividableBy7 = []

for i in range(100,200):
    if i % 7 == 0:
        dividableBy7.append(i)

i=0
for num in dividableBy7:
    i+=1
    print(num, end=" ")
    if i == 5:
        i=0
        print("\n", end="")