import plotly.graph_objects as go
import pandas as pd

# 데이터 생성
x = [1, 2, 3, 4, 5]
y = [10, 11, 12, 13, 14]

# Figure 객체 생성
fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=y, mode='markers'))

# 테이블 생성
data = {'x': x, 'y': y}
df = pd.DataFrame(data)
table = go.Figure(data=[go.Table(header=dict(values=list(df.columns)),
                                 cells=dict(values=[df[col] for col in df.columns]))
                        ])


# 이벤트 핸들러 함수
def handle_click(trace, points, state):
    # 선택한 항목의 인덱스 가져오기
    selected_indices = [point['pointIndex'] for point in points]

    # 선택한 항목에 대한 정보 업데이트
    selected_data = df.iloc[selected_indices]
    state['data'] = selected_data

    # 테이블 업데이트
    table.data[0].cells.values = [selected_data[col] for col in selected_data.columns]


# 이벤트 핸들러 추가
fig.data[0].on_click(handle_click, {'data': None})

# 레이아웃 업데이트
fig.update_layout(
    title="Select items to see the table",
    annotations=[dict(
        text="",
        x=0.5,
        y=1.1,
        showarrow=False,
        font=dict(size=16)
    )]
)

# 차트 및 테이블 표시
fig.show()
table.show()

''''
테이블 만 표시
'''
