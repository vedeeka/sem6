from matplotlib import pyplot as plt

def lets_go(bits, voltage):
    x=[0]
    y=[0]



    for i,b in enumerate(bits):
        if b=='1':
           y+=[-voltage,-voltage]
           x+=[i,i+1]
        else:
            y+=[voltage,voltage]
            x+=[i,i+1]
        


    plt.step(x,y,where='post')
    plt.grid()
    plt.show()       





Bits = input("Enter the bits: ")
voltage = float(input("Enter the voltage: "))
lets_go(Bits,voltage)