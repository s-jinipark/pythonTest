# express 패키지를  px로 불러옴
import plotly.express as px

# px.bar() 함수를 활용해서 bar chart 생성과 동시에 Data, Layout 값 입력
fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2],title="A Figure Specified By express")

#show하면 내 노트북 (주피터 노트북 등)에 그래프가 나타남.
fig.show()
