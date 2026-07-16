#AMI (Alternate Mark Inversion): 0 = 0 V, while successive 1s alternate between +V and −V.
import matplotlib.pyplot as plt

def ami(bits, v):
    x, y = [0], [0]
    p = -v

    for i in range(len(bits)):
        if bits[i] == '1':
            p = -p
            y += [p, p]
        else:
            y += [0, 0]
        x += [i, i + 1]

    plt.step(x, y, where='post')
    plt.grid()
    plt.show()

ami(input("Bits: "), float(input("Voltage: ")))