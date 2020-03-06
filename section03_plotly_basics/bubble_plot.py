# import classes, libraries and functions
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Import key data
df = pd.read_csv('data/mpg.csv')
print(df.head())
print(df.columns)

# Data object - create data object
data = [go.Scatter(x=df['horsepower'],
                   y=df['mpg'],
                   text=df['name'],
                   mode='markers',
                   marker= dict(
                        size=df['weight']/100,
                        color=df['cylinders'],
                        showscale=True
                   ))]

# Create layout object
layout = go.Layout(title='Bubble Chart',
                   hovermode='closest')

# Create figure object
fig = go.Figure(data=data, layout=layout)

# Plot the graph
pyo.plot(fig, filename="bubble_plot.html")
