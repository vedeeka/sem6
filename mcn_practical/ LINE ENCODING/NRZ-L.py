#NRZ-L (Non-Return-to-Zero-Level): Signal level depends on the bit value (0 = +V, 1 = −V).
import matplotlib.pyplot as plt

def nrz_l(bits, v):
    x = [0]
    level = v if bits[0] == '0' else -v
    y = [level]

    for i, b in enumerate(bits):
        level = v if b == '0' else -v
        x += [i, i+1]
        y += [level, level]

    plt.step(x, y, where='post')
    plt.grid(True)
    plt.axhline(0, color='black')
    plt.show()

nrz_l(input("Bits: "), float(input("Voltage: ")))