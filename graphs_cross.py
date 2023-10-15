import matplotlib.pyplot as plt
import numpy as np


def plots(y1='3x+7', y2='-2x-3'):
    plt.title("Пересечение графиков")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(visible=True, which='major', axis='both')
    x = np.linspace(-20, 20, 80)
    y1 = y1.split('x')
    fx1 = [int(y1[0]) * i + int(y1[1]) for i in x]
    y2 = y2.split('x')
    fx2 = [int(y2[0]) * i + int(y2[1]) for i in x]
    plt.plot(x, fx1, x, fx2)
    plt.show()


plots()
plots(y1='2x+1', y2='-3x+10')
