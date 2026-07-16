#Manchester Encoding: There is always a transition in the middle of each bit; 0 = Low→High, 1 = High→Low.
import matplotlib.pyplot as plt

def manchester(bits):
    x, y = [], []

    for i, b in enumerate(bits):
        if b == '0':
            first, second = 0, 1      # Low → High
        else:
            first, second = 1, 0      # High → Low

        x += [2*i, 2*i+1]
        y += [first, first]

        x += [2*i+1, 2*i+2]
        y += [second, second]

    plt.step(x, y, where='post')
    plt.yticks([0, 1], ["LOW", "HIGH"])
    plt.grid()
    plt.show()

manchester(input("Enter bits: "))