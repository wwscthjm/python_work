"""Scatter Square Sequence"""

import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x ** 2 for x in x_values]
plt.scatter(x_values, y_values, s=40, c=y_values, cmap=plt.cm.Blues)

# Set figure title and x-y label
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set scale size
plt.tick_params(axis='both', which='major', labelsize=14)

# Set axis limits
plt.axis([0, 1100, 0, 1100000])

# plt.show()
plt.savefig('squares_plot.png', bbox_inches='tight')
