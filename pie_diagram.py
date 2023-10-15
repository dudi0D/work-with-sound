import matplotlib.pyplot as plt
import numpy as np


def graph(n: int):
    a = np.random.randint(0, 30, n)
    plt.pie(a)
    plt.show()


graph(7)