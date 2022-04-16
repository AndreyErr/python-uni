"""
>>> to_base(31, 16)
'1F'
>>> to_base(0, 3)
'0'
>>> to_base(-1, 3)
'0'
>>> to_base(-10, 3)
'0'
>>> to_base(125498451, 20)
'1J4762B'
>>> to_base(1254984, 100)
Traceback (most recent call last):
        ...
IndexError: string index out of range
"""
import string
def to_base(n, radix):
    if n > 0:
        digits="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        r=""
        while(n>0):
            k=n%radix   # очередная цифра
            r=digits[k]+r # приклеим к результату
            n=n//radix
        return r
    else:
        return "0"