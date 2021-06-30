import pandas as pd
import plotly.express as px
import csv

with open("coffee.csv") as f:
    df = csv.DictReader(f)
    figure = px.scatter(df, x = "Coffee", y = "Sleep", color = "Week")
    figure.show()

