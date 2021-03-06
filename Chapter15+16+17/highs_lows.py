"""Analyse CSV file"""

import csv
from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib import dates as mdates

# Obtain date, max and min temperature from file
filename = 'sitka_weather_2014.csv'
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
plt.title("Daily high and low temperatures, 2014", fontsize=24)
plt.xlim([datetime(2014, 1, 1), datetime(2014, 12, 22)])
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))  # datetime format, b is month in short
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())  # datetime interval
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.yticks(range(10, 80, 10))  # temperature limits and interval
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', direction='in', labelsize=16)

xlm = plt.gca().get_xlim()
xtk = plt.gca().get_xticks()
ylm = plt.gca().get_ylim()
ytk = plt.gca().get_yticks()

x2 = plt.gca().twiny()
x2.xaxis_date()
x2.set_xlim(xlm)
x2.set_xticks(xtk)
x2.set_xticklabels([])
plt.tick_params(axis='x', which='major', direction='in')

y2 = plt.gca().twinx()
y2.set_ylim(ylm)
y2.set_yticks(ytk)
y2.set_yticklabels([])
plt.tick_params(axis='y', which='major', direction='in')

plt.show()
