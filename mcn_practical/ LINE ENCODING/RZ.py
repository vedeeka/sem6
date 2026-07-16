import matplotlib.pyplot as plt

def rz(bits, v):
    x = []
    y = []

    for i, bit in enumerate(bits):
        level = v if bit == '1' else -v

        x.extend([i, i+0.5, i+0.5, i+1])
        y.extend([level, level, 0, 0])

    plt.step(x, y, where='post')
    plt.grid(True)
    plt.axhline(0, color='black')
    plt.xlim(0, len(bits))
    plt.ylim(-v-1, v+1)
    plt.show()

bits = input("Bits: ")
voltage = float(input("Voltage: "))

rz(bits, voltage)