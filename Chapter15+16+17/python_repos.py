"""Respond to Github API"""

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Execute API and save respond
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# Store respond in a variable
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# Dig info from Repo
repo_dicts = response_dict['items']

names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# Visualization
my_style = LS('#333366', base_style=LCS)

# font_size is now in class Style not class Config
my_style.title_font_size = 24  # default 16
my_style.label_font_size = 14  # default 10
my_style.major_label_font_size = 18  # default 10

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = "Most-Starred Python Projects on Github"
chart.x_labels = names
chart.add('', stars)
chart.render_to_file('python_repos.svg')
