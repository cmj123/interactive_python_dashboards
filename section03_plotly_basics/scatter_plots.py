# Scatter plot basic.py
# Import key libraries, classes and functions
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

# Create a rondom data setting
np.random.seed(42)
random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

# Data Object -Define data for plotly plot
data = [go.Scatter(x=random_x,
                   y=random_y,
                   mode='markers',
                   marker=dict(
                    size=12,
                    color='rgb(51,204,153)',
                    symbol='pentagon',
                    line=dict(width=2)
                   ))]

# Layout Object - Define the layout for plotly
layout = go.Layout(title='Hello First Plot',
                   xaxis=dict(title='MY X AXIS'),
                   yaxis=dict(title='MY Y AXIS'),
                   hovermode='closest')

# Create figure for the plot
fig = go.Figure(data=data, layout=layout)
# Create plot
pyo.plot(data, filename='scatter.html')
