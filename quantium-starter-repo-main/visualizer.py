import pandas as pd
from dash import Dash, html, dcc
from plotly.express import line
df = pd.read_csv('result.csv')
df= df.sort_values(by="date")
dash_app = Dash(__name__)

chart = line(df, x="date", y="sales", title="Pink Morsel",color='region')
visualization = dcc.Graph(
    id="visualization",
    figure=chart
)

# create the header
header = html.H1(
    "Pink Morsel chart",
    id="header"
)

# define the app layout
dash_app.layout = html.Div(
    [
        header,
        visualization
    ]
)

# this is only true if the module is executed as the program entrypoint
if __name__ == '__main__':
    dash_app.run_server()