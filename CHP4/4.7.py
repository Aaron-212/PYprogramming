'''
File: 4.7.py
File Created: 2023/09/18 23:19:20
Author: Aaon212 (aaron212cn@outlook.com)

Copyright 2023 Aaron212
'''
import hashlib

name = input("Enter Username >>>")
if name == "admin":
    tries = 0
    while tries<3:
        data = input("Enter Password >>>")
        data_sha = hashlib.sha256(data.encode("utf-8")).hexdigest()
        encd_sha = "e0bebd22819993425814866b62701e2919ea26f1370499c1037b53b9d49c2c8a"
        if data_sha == encd_sha:
            break
        else:
            print("Wrong Password")
            tries+=1
    if tries<3:
        print("Welcome Admin")
    else:
        print("Too many tries")
else:
    print("Wrong Username")