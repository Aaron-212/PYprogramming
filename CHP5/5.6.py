'''
File: 5.6.py
File Created: 2023/09/18 23:50:54
Author: Aaon212 (aaron212cn@outlook.com)

Copyright 2023 Aaron212
'''

def delStr(s1, s2):
    if len(s1)>len(s2):
        raise Exception("s1 is longer than s2")
    for i in range(1, len(s2)-len(s1)):
        if s2[i:i+len(s1)] == s1:
            return s2[:i] + s2[i+len(s1):]

s1 = input("Input s1 >>>")
s2 = input("Input s2 >>>")

print(delStr(s1, s2))