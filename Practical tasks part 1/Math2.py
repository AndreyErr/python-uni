from math import *


def main(z):
    sum_i = 0
    for i in range(1, len(z) + 1):
        sum_i += (log(34*z[floor(i/3)] + 65*z[floor(i/3)]**3+10)**6) / (91)
    return sum_i


print(main([-0.07, -0.93]))
print(main([-0.13, 0.61]))
