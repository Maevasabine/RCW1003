import dash 
from dash import html, dcc
app= dash.Dash(__name__,requests_pathname_prefix='/dashboard/')
app.layout= html.Div(children=[
    html.Div([ 
    html.A('Home', href='/'),
    ],style={'marginTop':20}),
    
    dcc.Graph(
        id="example-graph",
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'example 1'},
                {'x': [7, 2, 5], 'y': [2, 4, 5], 'type': 'bar', 'name': 'example 2'}
            ],
            
        }
    )

])