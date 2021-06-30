import plotly.express as px
import csv
import numpy as np 

def getDataSource(data_path):
    icecream_sales = []
    colddrink_sales = []
    with open(data_path) as b:
        csv_reader = csv.DictReader(b)
        for row in csv_reader:
            icecream_sales.append(float(row["Temperature"]))
            colddrink_sales.append(float(row["Ice-cream Sales"]))
    return{"x":icecream_sales,"y":colddrink_sales}

def findCoorelation(datasource):
    coorelation = np.corrcoef(datasource["x"],datasource["y"])
    print("Coorelation between temperature and ice cream sales is: "+ coorelation[0,1])