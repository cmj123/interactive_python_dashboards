# Import key libraries, classes, and functions
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

# Set the random numpy seed state
x_values = np.linspace(0,1,100)
y_values = np.random.randn(100)

# Add different line graphs as trace
## Graph traces
trace0 = go.Scatter(x=x_values,
                   y=y_values+5,
                   mode='markers',
                   name='Markers')

trace1 = go.Scatter(x=x_values,
                    y= y_values,
                    mode='lines',
                    name='Lines')

trace2 = go.Scatter(x=x_values,
                    y= y_values-5,
                    mode='lines+markers',
                    name='Lines + Markers')

# List of traces - Add multiple plots
data = [trace0, trace1, trace2]

# Layout object
layout = go.Layout(title='Line Charts')

# Fig Object
fig =go.Figure(data=data, layout=layout)

# Plot figure
pyo.plot(data, filename='line_charts.html')
