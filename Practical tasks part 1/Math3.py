def x1(cond, c2, x):
    if (cond == 'HLSL'):
        return 0
    elif (cond == "LEAN"):
        return 1
    if(c2 == 1993):
        return 2
    elif (c2 == 1962):
        return 3
    return 4


def main(x):
    if (x[1] == 1981):
        if(x[0] == 'LIMBO'):
            return x1(x[3], x[2], 0)
        elif (x[0] == 'NESC'):
            return 5
        if (x[3] == 'HLSL'):
            return 6
        elif (x[3] == 'LEAN'):
            return 7
        if (x[2] == 1993):
            return 8
        elif (x[2] == 1962):
            return 9
        return 10
    elif (x[1] == 2000):
        return 11
    return 12


X = ['NESC', 1982, 1961, 'LEAN', 2006]
Y = ['LIMBO', 1981, 1993, 'MUF', 1989]
print(main(X))
print(main(Y))
