#Low volt is assigned for logical 0 bit and for logical 1 it returns to zero in the middle of the bit. 1 : positive-to-zero, 0 : zero.
import matplotlib.pyplot as plt

def rz_unipolar(bits, v):
    x, y = [], []

    for i, b in enumerate(bits):
        if b == '1':
            x += [i, i+0.5, i+0.5, i+1]
            y += [v, v, 0, 0]
        else:
            x += [i, i+1]
            y += [0, 0]

    plt.step(x, y, where='post')

    plt.yticks([0, v], ["0", "+V"])        
    plt.xlabel("Bits")
    plt.ylabel("Voltage")
    plt.title("RZ Unipolar Encoding")
    plt.grid(True)
    plt.show()

rz_unipolar(input("Bits: "), float(input("Voltage: ")))