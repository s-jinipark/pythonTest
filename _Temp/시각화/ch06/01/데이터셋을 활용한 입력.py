import plotly.express as px

# 데이터 불러오기
df = px.data.iris()

print(df)

fig = px.scatter(data_frame=df, x="sepal_width", y="sepal_length")

fig.show()
