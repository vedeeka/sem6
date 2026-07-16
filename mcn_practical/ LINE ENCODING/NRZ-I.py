#NRZ-I (Non-Return-to-Zero-Inverted): A 1 causes a transition; 0 causes no change.
import matplotlib.pyplot as plt

def nrz_i(bits, v):
    x, y = [0], [-v]
    level = -v

    for i, b in enumerate(bits):
        if b == '1':
            level = -level          # Toggle for 1
        x += [i, i+1]
        y += [level, level]

    plt.step(x, y, where='post')
    plt.grid()
    plt.show()

nrz_i(input("Bits: "), float(input("Voltage: ")))