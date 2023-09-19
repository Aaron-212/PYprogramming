'''
File: 5.8.py
File Created: 2023/09/19 08:22:12
Author: Aaon212 (aaron212cn@outlook.com)

Copyright 2023 Aaron212
'''

# 同4.9

def gcd(m, n):
    t = 1
    while t != 0:
        t = m % n
        m = n
        n = t
    return m


m, n = map(int, input("Enter two integers >>>").split())
print("GCD:", gcd(m, n))
