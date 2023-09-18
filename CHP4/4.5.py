'''
File: 4.5.py
File Created: 2023/09/18 23:13:02
Author: Aaon212 (aaron212cn@outlook.com)

Copyright 2023 Aaron212
'''

i, j = 4, 1
for i in range(4, 1000):
    temp = 0
    for j in range(1, i):
        if i % j == 0:
            temp += j
    if temp == i:
        print(f"{i} = 1", end="")
        for j in range(2, i):
            if i % j == 0:
                print(f"+{j}", end="")
        print()
