from plotly.subplots import make_subplots

# subplot 생성
fig = make_subplots(rows=1, cols=2)

# Trace 추가하기
fig.add_scatter(y=[4, 2, 3.5], mode="markers",
                marker=dict(size=20, color="LightSeaGreen"),
                name="a", row=1, col=1)

fig.add_bar(y=[2, 1, 3],
            marker=dict(color="MediumPurple"),
            name="b", row=1, col=1)

fig.add_scatter(y=[2, 3.5, 4], mode="markers",
                marker=dict(size=20, color="MediumPurple"),
                name="c", row=1, col=2)

fig.add_bar(y=[1, 3, 2],
            marker=dict(color="LightSeaGreen"),
            name="d", row=1, col=2)

# 한번에 Bar plot 만 파란색으로 바꾸기
# fig.update_traces(marker=dict(color="RoyalBlue"),
#                   selector=dict(type="bar"))

fig.show()