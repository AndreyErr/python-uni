import math


def main(z):
    n = len(z)
    sum_i = 0
    for i in range(1, n+1):
        sum_i += z[n - math.ceil(i / 2)] ** 4 / 67
    return sum_i


print(main(4))
print(main(5))