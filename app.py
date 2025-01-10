from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import duckdb

con = duckdb.connect("data/db/match_tracking.duckdb", read_only=True)

shotDirectionDF = con.sql("select * from stg.shot_direction").df()

app = Dash()

app.layout = [
    html.H1(children='Player Shot Preference', style={'textAlign':'center'}),
    dcc.Dropdown(shotDirectionDF.player.unique(), 'Carlos Alcaraz', id='player-selection'),
    dcc.Graph(id='shot-content')
]

@callback(
    Output('shot-content', 'figure'),
    Input('player-selection', 'value')
)
def update_graph(value):
    playerShotDirectionDF = shotDirectionDF[shotDirectionDF.player == value]
    return px.bar(playerShotDirectionDF, x='shotType', y='shotCount')

if __name__ == '__main__':
    app.run(debug=True)