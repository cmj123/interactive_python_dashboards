# Import classes, library, and classes
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Import data
df = pd.read_csv('data/2018WinterOlympics.csv')
# print(df.head())

# Create the data object
# data = [go.Bar(x=df['NOC'],
#                y=df['Total'],
#                name='2018 Winter Olympics')]

trace1 = go.Bar(x=df['NOC'],
               y=df['Gold'],
               name='Gold',
               marker={'color':'#FFD700'})

trace2 = go.Bar(x=df['NOC'],
               y=df['Silver'],
               name='Silver',
               marker={'color':'#9EA0A1'})

trace3 = go.Bar(x=df['NOC'],
               y=df['Bronze'],
               name='Bronze',
               marker={'color':'#CD7F32'})

# Set the data object
data = [trace1, trace2, trace3]

# Create the layout object
layout = go.Layout(title='2018 Winter Olympics', barmode='stack')

# Fig Object
fig =go.Figure(data=data, layout=layout)

# Plot object
pyo.plot(fig, filename='bar_chart.html')
