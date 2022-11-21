
import plotly.express as px
import pandas as pd
# Loading the iris dataset
df =pd.read_csv('result.csv')
fig = px.line(df, x = "date", y = "sales",
              color = "region")
fig.show()