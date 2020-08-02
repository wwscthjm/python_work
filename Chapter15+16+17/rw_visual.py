"""Draw Random Walk Points"""

import matplotlib.pyplot as plt
import pygal

from random_walk import RandomWalk


# Nonstop running random walk as long as the program is active
while True:
    # Create a case for RandomWalk, and draw its all points
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Set window size
    plt.figure(figsize=(10, 6), dpi=128)

    plt.plot(rw.x_values, rw.y_values, linewidth=1)
    # plt.scatter(rw.x_values, rw.y_values, s=15, c=range(rw.num_points), cmap=plt.cm.Blues)

    # Highlight start and stop point
    plt.scatter(0, 0, s=100, c='green')
    plt.scatter(rw.x_values[-1], rw.y_values[-1], s=100, c='red')

    # Hide axes
    plt.gca().get_xaxis().set_visible(False)
    plt.gca().get_yaxis().set_visible(False)

    # Following axes hiding methods may cause Warnings:
    # MatplotlibDeprecationWarning: Adding an axes using the same arguments as a previous axes currently reuses the
    # earlier instance.  In a future version, a new instance will always be created and returned.  Meanwhile, this
    # warning can be suppressed, and the future behavior ensured, by passing a unique label to each axes instance.
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)

    plt.show()

    xy_chart = pygal.XY()
    xy_chart.add("Random Walk", [(rw.x_values[x], rw.y_values[x]) for x in range(rw.num_points)])
    xy_chart.render_to_file("random_walk.svg")

    keep_running = input("Make another walk? (y/n):")
    if keep_running == 'n':
        break
