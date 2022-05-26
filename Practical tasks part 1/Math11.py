from struct import unpack


def main(file):
    # Find starting address
    signature = bytes([0xcf, 0x46, 0x52, 0x42, 0x4b])
    a_adr = file.find(signature) + len(signature)

    # Unpack data for structure A
    a = {f'A{i}': None for i in range(1, 6)}
    temp = unpack('<7sLLdB', file[a_adr:a_adr + 24])
    a['A1'] = str(temp[0], 'utf8')
    b_adr, d_adr, a['A4'], a['A5'] = temp[1:]

    # Unpack data for structure B
    b = {f'B{i}': None for i in range(1, 8)}
    temp = unpack('<hLHQ2BH3bQ', file[b_adr:b_adr + 31])
    b['B1'], c_size, c_adr, b['B3'] = temp[0:4]
    b['B4'] = list(temp[4:6])
    b['B5'] = temp[6]
    b['B6'] = list(temp[7:10])
    b['B7'] = temp[10]

    b['B2'] = []
    for i in range(c_size):
        temp = unpack('<hHI', file[c_adr + 8 * i:c_adr + 8 * (i + 1)])
        num, arr_size, arr_adr = temp
        temp = unpack(f'<{arr_size}i', file[arr_adr:arr_adr + arr_size * 4])
        b['B2'].append({'C1': num, 'C2': list(temp)})

    # Unpack data for structure D
    d = {f'D{i}': None for i in range(1, 3)}
    temp = unpack(f'<ld', file[d_adr:d_adr + 12])
    d['D1'], d['D2'] = temp

    # Assign structures B and D to A2 and A3
    a['A2'] = b
    a['A3'] = d
    return a


# --- cut this out when submitting to robot ---
data1 = (
    b'\xcfFRBKkvhqrrgY\x00\x00\x00x\x00\x00\x000COi\xe7#\xcb?!\x9d\x14\x1a3P\x05N'
    b'\x92\xfa\xe5\\U\xb6H\xd3V<\xda\\(\x82\x8b\xd5\xc0\x7fS\xd3?\xa0\x88\xef'
    b'\xde)2\xd9\xe1\x0e\x0e\x02\x00\x1d\x00\x00\x001\x12\x03\x00%\x00\x00'
    b'\x00`\xdd\x04\x001\x00\x00\x00\x87\xe4\x03\x00\x00\x00A\x00Y\x00\x04'
    b'\x7f\xc8o\xab\xf2\xaf\x99(gS\xac\xa5y:\xed}z\x08K\xee\x82\xdbH\xfc\xd4\xcddc'
    b'\xef`\xe4\xbf'
)

data2 = (
    b'\xcfFRBKixojucfE\x00\x00\x00d\x00\x00\x00p\xe8`\xaa\x96x\xee?\xff\xdc\x01}'
    b"@$>1\xcb\xe3\xa9\x8d\xc8*\xb0\x1d\xb1\xaf\x1e\xfb_\xa8`'PO\xcc\x02"
    b'\x00\x1d\x00\x00\x00\x17c\x04\x00%\x00\x00\x00i\xd4\x02\x00\x00\x005'
    b'\x00\xbd\x0e\xa7\x05/h\xf1\xa4Y\xd9\x1a\x1a\xb4\x91\x10\xc8 w\xbb'
    b'\x01\x03\xaa\xe9\xee\xf0h\x96\x94\xe17\x182\xa9\xd9?'
)

print(main(data1))
print(main(data2))