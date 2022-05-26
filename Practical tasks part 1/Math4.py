def main(x):
    g_bit = 0b10000000000000000000000000000000
    f_bit = 0b01110000000000000000000000000000
    e_bit = 0b00001111000000000000000000000000
    d_bit = 0b00000000111111100000000000000000
    c_bit = 0b00000000000000011110000000000000
    b_bit = 0b00000000000000000001111110000000
    a_bit = 0b00000000000000000000000001111111

    new_a = (x & a_bit) << 25
    new_b = (x & b_bit) >> 7
    new_c = (x & c_bit) >> 3
    new_d = (x & d_bit) << 1
    new_e = (x & e_bit) >> 18
    new_f = (x & f_bit) >> 14
    new_g = (x & g_bit) >> 14

    res = new_a | new_b | new_c | new_d | new_e | new_f | new_g
    return res


print(hex(main(0x44e12479)))

print(hex(main(0x6de0a758)))