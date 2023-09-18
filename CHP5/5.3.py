'''
File: 5.3.py
File Created: 2023/09/18 23:36:12
Author: Aaon212 (aaron212cn@outlook.com)

Copyright 2023 Aaron212
'''

def factorial(x):
    if x <= 1:
        return 1
    else:
        fact = 1
        for i in range(2,x+1):
            fact*=i
        return fact
    
def C(n, m):
    return int(factorial(n)/(factorial(m)*factorial(n-m)))

m, n = map(int, input("Enter two integers >>>").split())
print("C:", C(m, n))
