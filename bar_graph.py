import matplotlib.pyplot as plt
import numpy as np

plt.title('Владение языками программирования среди опрошенных')
plt.ylabel('кол-во чел.', loc='top')
plt.grid(True)
x = ['Python', 'C/C++', 'Perl', 'Java', 'C#', 'Go', 'R']
y = np.random.randint(0, 1000, 7)
plt.bar(x, y)
plt.show()
