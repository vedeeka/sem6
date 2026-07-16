#Pseudoternary: 1 = 0 V, while successive 0s alternate between +V and −V.
import matplotlib.pyplot as plt

def pseudoternary(bits, v):
    x, y = [0], [0]
    level = -v

    for i, b in enumerate(bits):
        if b == '0':
            level = -level      # Toggle for 0
        else:
            level = 0

        x += [i, i+1]
        y += [level, level]

        if b == '1':
            level = -level      # Restore previous polarity

    plt.step(x, y, where='post')
    plt.grid()
    plt.show()

pseudoternary(input("Bits: "), float(input("Voltage: ")))