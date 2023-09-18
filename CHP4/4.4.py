'''
File: 4.4.py
File Created: 2023/09/18 23:10:15
Author: Aaon212 (aaron212cn@outlook.com)

Copyright 2023 Aaron212
'''

import numpy as np

i = int(input("Input i >>>"))

for iter in range(1, i//2+1):
    if i%iter == 0:
        print(iter, end=" ")