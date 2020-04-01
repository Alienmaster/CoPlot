import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
import os, csv
import numpy as np
import argparse
import collections
import inspect

##### init #####
os.chdir("COVID-19/csse_covid_19_data/csse_covid_19_time_series")

cases = collections.defaultdict(list)
growth = collections.defaultdict(list)
deaths = collections.defaultdict(list)
description = []
country= "Germany"

##### Argument parser #####
parser = argparse.ArgumentParser(description="COVID-19 Data Visualisation Tool")
parser.add_argument("-c", "--country", metavar="Germany", type=str, help="Name of the state (eg. US, Germany)", required=True)
parser.add_argument("-t", "--timerange", metavar="14", type=int, help="Show the range of the last x days in the data. Default is 14", default=14)
parser.add_argument("-d", "--death", type=bool, metavar ="True", help="Show the deaths in the Chart. Default is True", default=True)
args = parser.parse_args()
country = args.country
timeRange = args.timerange
showDeath = args.death


##### read file #####
with open("time_series_covid19_confirmed_global.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    description = csv_reader.__next__()
    for row in csv_reader:
        for t in row[4:len(row)]:
            if row[0] == "":
                cases[row[1]].append(int(t))
            else:
                cases[row[0]].append(int(t))

if showDeath:
    with open("time_series_covid19_deaths_global.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        description = csv_reader.__next__()
        for row in csv_reader:
            for t in row[4:len(row)]:
                if row[0] == "":
                    deaths[row[1]].append(int(t))
                else:
                    deaths[row[0]].append(int(t))

if timeRange > len(description[4:]):
    timeRange = len(description[4:])

##### calculate growth #####
for e in cases:
    for previous, current in zip(cases[e], cases[e][1:]):
        growth[e].append(current - previous)

##### plotting Graph #####
fig, ax = plt.subplots(figsize=(7.5, 7.5))
ax.set(title="COVID-19 Cases and growth in %s for the last %s days" % (country, timeRange) )
ax.set_xlabel("Days")
axes = [ax, ax.twinx()]
axes[1].set_frame_on(True)
axes[1].patch.set_visible(False)
p1 = axes[0].bar(description[-timeRange:], deaths[country][-timeRange:], color="tab:gray")
p2 = axes[0].bar(description[-timeRange:], cases[country][-timeRange:], bottom=deaths[country][-timeRange:])
blue_patch = mpatches.Patch(color='tab:blue', label="active cases") # legend
gray_patch = mpatches.Patch(color='tab:gray', label="deaths") # legend
axes[1].plot(growth[country][-timeRange:], "tab:red")
blue_line = mlines.Line2D([], [], color='tab:red', markersize=15, label='New infections')
axes[0].set_ylabel("All cases")
axes[0].tick_params(axis="x", rotation=90)
axes[1].set_ylabel("New infections")
plt.legend(handles=[blue_patch, gray_patch, blue_line], loc="upper left")
plt.savefig("../../../%s.png" % country)
plt.show()
