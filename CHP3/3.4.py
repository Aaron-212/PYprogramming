'''
File: 3.4.py
File Created: 2023/09/18 22:11:58
Author: Aaon212 (aaron212cn@outlook.com)

Copyright 2023 Aaron212
'''

G = 6.67408e-11
mass1 = float(input("Input mass1 >>>"))
mass2 = float(input("Input mass2 >>>"))
r = float(input("Input distance >>>"))

F = G * mass1 * mass2 / (r**2)

print(f"Gravitational force is {F} N")