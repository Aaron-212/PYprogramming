'''
File: 4.6.py
File Created: 2023/09/18 23:16:37
Author: Aaon212 (aaron212cn@outlook.com)

Copyright 2023 Aaron212
'''

def kx(x):
    return (1/16**x*( 4/(8*x+1) - 2/(8*x+4) - 1/(8*x+5) - 1/(8*x+6) ))

sum = 0
for i in range(0,100):
    sum+=kx(i)
    
print(f"Pi is roughly equal to {sum}")