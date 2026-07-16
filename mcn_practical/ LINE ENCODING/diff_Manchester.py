#Differential Manchester Encoding: There is always a middle transition; 0 has an extra transition at the beginning, 1 has none.
import matplotlib.pyplot as plt

def diff_manchester(bits):
    x, y = [], []
    level = 1      # Starting level

    for i, b in enumerate(bits):

        if b == '0':
            level = 1 - level      # Transition at beginning for 0

        x += [2*i, 2*i+1]
        y += [level, level]

        level = 1 - level          # Always transition in middle

        x += [2*i+1, 2*i+2]
        y += [level, level]

    plt.step(x, y, where='post')
    plt.yticks([0, 1], ["LOW", "HIGH"])
    plt.grid()
    plt.show()

diff_manchester(input("Enter bits: "))