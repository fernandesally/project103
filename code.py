import pandas as pd
import plotly.express as px

df=pd.read_csv("data.csv")
fig=px.scatter(df,x="date",y="cases",size="Percentage",color="country",size_max=60)
fig.show()

