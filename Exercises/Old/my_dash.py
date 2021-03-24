import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

data = pd.read_csv(r"F:\Programacion\1.BOOTCAMP\data\general_dfs\cars2.csv")

app = dash.Dash(__name__)

header = 'Australia fires'
subtitle = 'Analyze the fires declared in Australia in 2019'
graph_title = 'Graph#1'
graph_title_2 = 'Graph#2'

graph_1_settings = {"x": data["cylinders"], "y": data["displacement"], "type": "bar"}
graph_2_settings = {"x": data["cylinders"], "y": data["displacement"], "type": "piechart", }

app.layout = html.Div(
    children=[
        html.H1(children= header, ),
        html.P(children= subtitle, ),

        dcc.Graph(figure={"data": [graph_1_settings], 
                        "layout": {"title": graph_title}, },),

        dcc.Graph(figure={"data": [graph_2_settings], 
                        "layout": {"title": graph_title_2}, }, ),
    ])

if __name__ == "__main__":
    app.run_server(debug=True)