# Requirements:
* Python 3.8
* mathplotlib
* [JHU Repository](https://github.com/CSSEGISandData/COVID-19)

# Usage
* clone the JHU repository into the CoPlot Repo
`py.exe main.py -c Germany -t 20 -d False`
* `-c / --country` Select the country (required)
* `-t / --timerange` Select the last x days (default: 14)
* `-d / --deaths` Plot the deaths (default: True)


# Missing Features: 
* Compare multiple countrys at the same time
* Give a list of possible countrys
