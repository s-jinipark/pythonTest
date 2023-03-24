

import matplotlib.pyplot as plt
from random import  shuffle


xs = [x+1 for x in range(10000)]
ys = [y+1 for y in range(10000)]

shuffle(xs)
shuffle(ys)

plt.scatter(xs, ys, label="samples")
plt.show()