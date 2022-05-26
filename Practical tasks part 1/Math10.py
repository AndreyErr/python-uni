def main(table):
    parsed = set()
    state, percent, man, end1 = [], [], [], []
    for first, name1, name2 in table:
        if name1 in parsed or first is None:
            continue
        end = []
        parsed.add(name1)
        h1 = first.split(";")
        if (h1[0] == 'Да'):
            h1[0] = 'Выполнено'
        else:
            h1[0] = 'Не выполнено'
        h1[1] = h1[1] + '00'
        h2 = name1.split(" ")
        name1 = (f'{h2[0][0]}.{h2[1]} {h2[2]}')
        end.append(h1[0])
        end.append(h1[1])
        end.append(name1)
        end1.append(end)
    return end1


# --- cut this out when submitting to robot ---
t = [
    [None, None, None],
    [None, None, None],
    ['Да;0.9', 'Самир Г. Зизевян', 'Самир Г. Зизевян'],
    ['Да;0.4', 'Мирослав Б. Зашяк', 'Мирослав Б. Зашяк'],
    ['Да;0.4', 'Мирослав Б. Зашяк', 'Мирослав Б. Зашяк']
]
# main(t)
res = main(t)
print(res)
