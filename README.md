# aqdataUCI_api
API for [UCI Air Quality data - Italian City](https://archive.ics.uci.edu/ml/datasets/Air+Quality#) filtering and plot. Exercise proposed under Let's Code - Santander Coders Course.

## Author:
- <a href='https://github.com/samyadelara'>Samya de Lara Lins de Araujo Pinheiro</a>

## How to run the project - Python 3.7

1 - Clone repo

```
git clone https://github.com/samyadelara/aqdataUCI_api.git
```

2 - Change to project folder

```
cd aqdataUCI_api
```

3 - Create virtual env - using venv

```
python3.7 -m venv env
```

4 - Activate virtual environment

```
source env/bin/activate
```

5 - Install modules

```
pip install -r requirements.txt
```

6 - Activate API - locally

```
python3 api_aq_data.py
```

7 - Request data 
**(filters available year = 2004 or 2005)**
Use API get or HTML 
`http://127.0.0.1:5000/year/2004`
or
`http://127.0.0.1:5000/year/2005`

Filtered data will be aggregated as *Daily Means* and saved as .json and .csv format.
A HeatMap is prepared and saved as .png to illustrate the association between variables.

> Correlation is stronger (positive) between most of the pollutants, and is negative with NOx (one of its precursors). Temperature presented higher absolute correlation between nitrogen oxides (NOx and NO2) considering both filtered periods (2004:Mar-Dec and 2005:Jan-Apr).
