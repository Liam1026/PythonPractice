import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x**2

plt.figure()

plt.xlim((-1, 2))
plt.ylim((-2, 3))
plt.xlabel(' I am x')
plt.ylabel(' I am y')

new_sticks = np.linspace(-1, 2, 5)
plt.xticks(new_sticks)
plt.yticks([-2, -1.8, -1, 1.22, 3], [
    r'$really\ bad$', r'$bad\ \alpha$', r'$normal$', r'$good$',
    r'$really\ good$'
])

# !!!  , !!!  deliver to handles
l1, = plt.plot(x, y2, label='up')
l2, = plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--', label='down')
plt.legend(handles=[l1, l2], labels=['aaa', 'bbb'], loc='best')

plt.show()
