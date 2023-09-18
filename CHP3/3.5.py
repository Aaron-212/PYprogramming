'''
File: 3.5.py
File Created: 2023/09/18 22:16:29
Author: Aaon212 (aaron212cn@outlook.com)

Copyright 2023 Aaron212
'''

# a*x**2 + b*x + c =0
a = input("Input a >>>")
b = input("Input b >>>")
c = input("Input c >>>")

delta = b**2 - 4*a*c

if delta > 0:
    x1 = (-b + delta**0.5) / (2*a)
    x2 = (-b - delta**0.5) / (2*a)
    print(f"x1 = {x1}, x2={x2}")
elif delta == 0:
    x = -b / (2*a)
    print(f"x = {x}")
else:
    print("No real roots")