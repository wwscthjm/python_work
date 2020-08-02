"""Draw Random Walk Points"""

import matplotlib.pyplot as plt

from random_walk import RandomWalk


# Create a case for RandomWalk, and draw its all points
rw = RandomWalk()
rw.fill_walk()
plt.scatter(rw.x_values, rw.y_values, s=15)
plt.show()
