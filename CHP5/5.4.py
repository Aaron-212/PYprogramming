'''
File: 5.4.py
File Created: 2023/09/18 23:41:46
Author: Aaon212 (aaron212cn@outlook.com)

Copyright 2023 Aaron212
'''

def isLeapYear(x):
    if x % 4 != 0:
        return False
    if x % 400 == 0:
        return True
    if x % 100 == 0:
        return False
    return True

year = int(input("Input a year >>>"))
print(f"{year} is a leap year: {isLeapYear(year)}")