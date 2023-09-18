'''
File: 4.9.py
File Created: 2023/09/18 23:30:24
Author: Aaon212 (aaron212cn@outlook.com)

Copyright 2023 Aaron212
'''
def gcd(m, n):
    t = 1
    while t != 0:
        t = m % n
        m = n
        n = t
    return m

def lcm(m, n):
    return m * n // gcd(m, n)


m, n = map(int, input("Enter two integers >>>").split())
print("GCD:", gcd(m, n))
print("LCM:", lcm(m, n))
