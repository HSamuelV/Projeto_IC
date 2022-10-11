# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

arquivo_grande_area_uf = pd.read_csv("grande_area_uf.csv",sep=",",encoding="utf-8")

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame(arquivo_grande_area_uf)

fig = px.bar(df, x="UF", y='Linguistica, Letras e Artes',color='Linguistica, Letras e Artes', barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Linguistica, Letras e Artes por UF'),

    html.Div(children='''
        
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)


import pathlib
import dash
from dash import Dash, html, dcc, Input, Output, State, no_update
import dash_bootstrap_components as dbc
import plotly.express as px 
import pandas as pd

app = Dash(__name__, title="ICDashApp")

# Declare server for Heroku deployment. Needed for Procfile.
server = app.server

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options


PATH = pathlib.Path(__file__).parent

DATA_PATH = PATH.joinpath("data").resolve()

df = pd.read_csv(DATA_PATH.joinpath("grande_area_uf.csv"))

# make plot
fig = px.bar(df, x="UF", y='Linguistica, Letras e Artes',color='Linguistica, Letras e Artes', barmode="group")

# initialize app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.UNITED])

# set app layout
app.layout = html.Div(children=[
    html.H1(children='Linguistica, Letras e Artes por UF'),

    html.Div(children=''''''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])
if __name__ == "ICDashApp":
    app.run_server(debug=True)



