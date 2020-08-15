"""Download File"""

# import requests
# json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
# req = requests.get(json_url)
# # Write in file
# with open('btc_close_2017_urllib.json', 'w') as f:
#     f.write(req.text)
# # Load json format
# file_urllib = req.json()

import json
import pygal
import math
from itertools import groupby


def draw_line(x_data, y_data, title, y_legend):
    xy_map = []
    for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda _: _[0]):
        y_list = [v for _, v in y]
        xy_map.append([x, sum(y_list) / len(y_list)])
    x_unique, y_mean = [*zip(*xy_map)]
    line_chart_func = pygal.Line()
    line_chart_func.title = title
    line_chart_func.x_labels = x_unique
    line_chart_func.add(y_legend, y_mean)
    line_chart_func.render_to_file(title + '.svg')
    return line_chart_func


# Load data in a list
filename = 'btc_close_2017.json'
with open(filename) as f:
    btc_data = json.load(f)
# Save data
dates, months, weeks, weekdays, close = [], [], [], [], []
for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))

# line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
# line_chart.title = '收盘价对数变换（¥）'
# line_chart.x_labels = dates
# N = 20  # Step 20 days
# line_chart.x_labels_major = dates[::N]
# close_log = [math.log10(_) for _ in close]
# line_chart.add('log收盘价', close_log)
# line_chart.render_to_file('收盘价对数变换折线图（¥）.svg')

# idx_week = dates.index('2017-12-11')
# wd = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# week_int = [wd.index(w)+1 for w in weekdays[1:idx_week]]
# line_chart_month = draw_line(week_int, close[1:idx_week], '收盘价星期均值（¥）', '星期均值')
# line_chart_month

with open('收盘价DashBoard.html', 'w', encoding='utf8') as html_file:
    html_file.write('<html><head><title>收盘价DashBoard</title><meta charset="utf-8"></head><body>\n')
    for svg in ['收盘价折线图（¥）.svg', '收盘价对数变换折线图（¥）.svg', '收盘价月日均值（¥）.svg', '收盘价周日均值（¥）.svg',
                '收盘价星期均值（¥）.svg']:
        html_file.write('   <object type="image/svg+xml" data="{0}" height=500></object>\n'.format(svg))
    html_file.write('</body></html>')
