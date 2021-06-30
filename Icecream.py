import pandas as pd
import plotly.express as px
import csv

with open("sales.csv") as f:
    df = csv.DictReader(f)
    figure = px.scatter(df, x = "Temperature", y = "Ice-cream Sales", color = "Ice-cream Sales")
    figure.show()

