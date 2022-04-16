>>> from to_base import to_base
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