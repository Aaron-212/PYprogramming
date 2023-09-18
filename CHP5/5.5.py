'''
File: 5.5.py
File Created: 2023/09/18 23:45:29
Author: Aaon212 (aaron212cn@outlook.com)

Copyright 2023 Aaron212
'''

import numpy as np

def isPrime(x):
    for i in range(2, int(np.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

for i in range(2, 100):
    if isPrime(i):
        print(f"{i} is prime")