'''
File: 6.6.py
File Created: 2023/09/19 08:36:54
Author: Aaon212 (aaron212cn@outlook.com)

Copyright 2023 Aaron212
'''

def interval(t1, t2):
    # t = {"hour": xx, "minute": xx, "second": xx}
    s = t2["second"] - t1["second"]
    m = t2["minute"] - t1["minute"]
    h = t2["hour"] - t1["hour"]
    if s < 0:
        s += 60
        m -= 1
    if m < 0:
        m += 60
        h -= 1
    if h < 0:
        raise ValueError("invalid input, t2 should be later than t1")
    return {"hour": h, "minute": m, "second": s}

print(interval({"hour": 11, "minute": 30, "second": 36}, {"hour": 12, "minute": 31, "second": 24}))