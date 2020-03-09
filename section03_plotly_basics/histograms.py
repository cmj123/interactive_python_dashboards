# Import key libraries, classes and functions
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# Import dataset
df = pd.read_csv('data/mpg.csv')

# Create data object for histogram
# All data
# data = [go.Histogram(x=df['mpg'])]
# Data - Edit set range
data = [go.Histogram(x=df['mpg'], xbins=dict(start=0, end=50, size=2))]

# Create layout object for histogram
layout = go.Layout(title='Histogram')

# Create a fig
fig = go.Figure(data=data, layout=layout)

# Display the figure
pyo.plot(fig)
