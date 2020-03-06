# Import classes, functions and libraries
import plotly.offline as pyo
import plotly.graph_objs as go

# Dataset
# y = [1,14,14,15,16,18,18,19,19,20,20,23,24,26,27,27,28,29,33,54]
# data = [go.Box(y=y,
#                boxpoints='outliers',
#                jitter=0,
#                pointpos=0)]  # boxpoints='all' - show all outliers

snodgrass = [.209, .205, .196, .210, .202, .207, .224, .223, .220, .201]
twain =     [.225, .262, .217, .240, .230, .229, .235, .217]

# Create a data object
trace1 = go.Box(y=snodgrass,
               name='Snodgrass')

trace2 = go.Box(y=twain,
               name='Twain')


data = [trace1, trace2]  # boxpoints='all' - show all outliers

# Create a layout object
layout = go.Layout(title='Box Plot',
                    xaxis=dict(title='Box 1'))

# Create a figure object
fig = go.Figure(data=data,
                layout=layout)

# Plot object
pyo.plot(fig, filename='box_plot.html')
