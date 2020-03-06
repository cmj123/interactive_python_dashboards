# import library, classes and functions
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Import data
df = pd.read_csv('data/nst-est2017-alldata.csv')
# print(df.head())

# Filter data - get New England population data
df2 = df[df['DIVISION']=='1']
df2.set_index('NAME', inplace=True)
list_of_pop_col = [col for col in df2.columns if col.startswith('POP')]
# print(list_of_pop_col)
df2 = df2[list_of_pop_col]
# print(df2.head())

# List comprehension plotting
data = [go.Scatter(x=df.columns,
                   y=df2.loc[name],
                   mode='lines',
                   name=name) for name in df2.index]

# Plot data
pyo.plot(data, filename='line_charts2.html')
