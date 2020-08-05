"""Analyse CSV file"""

import csv
from datetime import datetime
from matplotlib import pyplot as plt

# Obtain date, max and min temperature from file
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)  # Return and pop out the next item

    dates, lows, highs = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, "missing data")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Draw figure from data
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5, label='high')
plt.plot(dates, lows, c='blue', alpha=0.5, label='low')
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Set figure's format
plt.title("Daily high and low temperatures, 2004\nDeath Valley", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.xlim(16070, 16426)
plt.legend()

plt.show()
