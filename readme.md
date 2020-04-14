# Requirements:
* Python 3.8
* mathplotlib
* [JHU Repository](https://github.com/CSSEGISandData/COVID-19)

# Usage
* clone the JHU repository into the CoPlot Repo
`py.exe main.py -c Germany -t 20 -d False`
* `-c / --Country` Select the country (required)
* `-t / --Timerange` Select the last x days (default: 14)
* `-d / --Deaths` Plot the deaths (default: True)
* `-v / --Verbose` Verbose Mode (default: False)

# Missing Features / Known Bugs: 
* Compare multiple countrys at the same time
* Give a list of possible countrys  
* The Country is Case sensitive (eg Italy, US)