"""Visualize a Die"""

import pygal

from die import Die


# Create a D6
die_1 = Die()
die_2 = Die(10)

# Roll it several times and store the results in a list
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyse the results
frequencies = []
for value in range(2, die_1.num_sides + die_2.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
hist = pygal.Bar()

hist.title = "Results of rolling one D6 and one D10 50,000 times."
hist.x_labels = [str(x) for x in range(2, 17)]
hist.x_title = "Results"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('die_visual.svg')
