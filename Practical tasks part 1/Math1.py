import math


def main(z):
    return ((18 * z - 70 * z**2 - 2) / (76 * (z - 0.02 - z**2)**3)) \
        - ((21 * math.cos(z) - z**4) / (61 * z**7))

print(main(1))
print(main(-0.45))
print(main(0.79))