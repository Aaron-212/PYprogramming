'''
File: 4.2.py
File Created: 2023/09/18 22:58:26
Author: Aaon212 (aaron212cn@outlook.com)

Copyright 2023 Aaron212
'''

import numpy as np

# A triangle
a = int(input("length a >>>"))
b = int(input("length b >>>"))
c = int(input("length c >>>"))

if a+b<c or a+c<b or b+c<a:
    raise ValueError("The triangle is not valid")
p = (a+b+c)/2
s = np.sqrt(p*(p-a)*(p-b)*(p-c))

print(f"The area of the triangle is {s}")