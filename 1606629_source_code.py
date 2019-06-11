import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
import plotly.graph_objs as go
import plotly.tools as tools
import plotly.plotly as ply


print(os.listdir("input"))
locations = pd.read_csv('input/kiva_mpi_region_locations.csv')
print(locations.head())


Y=locations.country.value_counts().index[::-1]
X=locations.country.value_counts().values[::-1]

data = go.Bar(
    x = X,
    y = Y,
    orientation = 'h',
    marker=dict(
        color=X,
        colorscale = 'Jet',
        reversescale = True
    ),
)

layout = go.Layout(
    title='Countries Around the world Kiva fund with Loans',
    width=800,
    height=1200,
    )
figure = go.Figure(data=[data], layout=layout)
ply.plot(figure, filename="LoansbyKiva")


Y=locations.world_region.value_counts().index[::-1]
X=locations.world_region.value_counts().values[::-1]
data = go.Bar(
    x = Y,
    y = X,
    orientation = 'v',
    marker=dict(
        color=X,
        colorscale = 'Jet',
        reversescale = True
    ),
)

layout = go.Layout(
    title='Regions Kiva Fund',
    width=700,
    height=500,
    )
figure = go.Figure(data=[data], layout=layout)
ply.plot(figure, filename="PerRegionLoans")






map_df = pd.DataFrame(locations['country'].value_counts()).reset_index()
map_df.columns=['country', 'loans']
map_df = map_df.reset_index().drop('index', axis=1)

data = [ dict(
        type = 'choropleth',
        locations = map_df['country'],
        locationmode = 'country names',
        z = map_df['loans'],
        text = map_df['country'],
        colorscale = [[0,"rgb(5, 50, 172)"],[0.85,"rgb(40, 100, 190)"],[0.9,"rgb(70, 140, 245)"],
            [0.94,"rgb(90, 160, 245)"],[0.97,"rgb(106, 177, 247)"],[1,"rgb(220, 250, 220)"]],
        autocolorscale = False,
        reversescale = True,
        marker = dict(
            line = dict (
                color = 'rgb(180,180,180)',
                width = 0.5
            ) ),
        colorbar = dict(
            autotick = False,
            tickprefix = '',
            title = 'Number of Loans'),
      ) ]

layout = dict(
    title = 'Number of Loans Per Country',
    geo = dict(
        showframe = False,
        showcoastlines = True,
        projection = dict(
            type = 'Mercator'
        )
    )
)

figure = dict( data=data, layout=layout )
ply.plot(figure, validate=False, filename='countryandloans')




trace = []
for name, group in locations.groupby("country"):

    trace.append ( 
        go.Box(
            x=group["MPI"].values,
            name=name
        )
    )
layout = go.Layout(
    title='Multidimensional Poverty Index(MPI) for earch Country',
    width = 1000,
    height = 2000
)
figure = go.Figure(data=trace, layout=layout)
ply.plot(figure, filename="ContryMPIndex")


trace = []
for name, group in locations.groupby("world_region"):

    trace.append ( 
        go.Box(
            y=group["MPI"].values,
            name=name
        )
    )
layout = go.Layout(
    title='Multidimensional Poverty Index(MPI) for each Region',
    width = 750,
    height = 800,
    orientation= 'v',
)
figure = go.Figure(data=trace, layout=layout)
ply.plot(figure, filename="WorldRegionMPI")



loans = pd.read_csv('input/kiva_loans1.csv')
Y=loans.activity.value_counts().index[::-1]
X=loans.activity.value_counts().values[::-1]
data = go.Bar(
    x = X,
    y = Y,
    orientation = 'h',
    marker=dict(
        color=X,
        colorscale = 'Jet',
        reversescale = True
    ),
)

layout = go.Layout(
    title='Loans by Activity',
    width=850,
    height=1000,
    )
figure = go.Figure(data=[data], layout=layout)
ply.plot(figure, filename="LoansSeries")


loans = pd.read_csv('input/construction.csv')
Y=loans.activity.value_counts().index[::-1]
X=loans.activity.value_counts().values[::-1]
data = go.Bar(
    x = X,
    y = Y,
    orientation = 'h',
    marker=dict(
        color=X,
        colorscale = 'Jet',
        reversescale = True
    ),
)

layout = go.Layout(
    title='Loans by Activity',
    width=850,
    height=1000,
    )
figure = go.Figure(data=[data], layout=layout)
ply.plot(figure, filename="LoansSeries2")

loans = pd.read_csv('input/Agriculture.csv')
X=loans.activity.value_counts()
trace = go.Pie(labels=X.index, values=X.values)
ply.plot([trace], filename='loans_in_agriculture_sector_by_activity')

loans = pd.read_csv('input/wholesale.csv')
X=loans.activity.value_counts()
trace = go.Pie(labels=X.index, values=X.values)
ply.plot([trace], filename='loans_in_wholesale_sector_by_activity')


trace0 = go.Scatter(
    x=region['country'].value_counts().index,
    y=region['country'].value_counts().values,
    text=region['country'].value_counts().index,
    mode='markers',
    marker=dict(
        color = np.random.randn(500), #set color equal to a variable
        colorscale='Jet',
        showscale=True,
        size=[i/5  if i < 550 else i/50 for i in region['country'].value_counts().values],
    )
)

data = go.Data([trace0])
ply.plot(data, filename='mpl-7d-bubble')


