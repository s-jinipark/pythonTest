import plotly.graph_objs as go
from plotly.subplots import make_subplots
import pandas as pd

# 데이터 생성
x = [1, 2, 3, 4, 5]
y = [10, 11, 12, 13, 14]

# Figure 객체 생성
fig = go.Figure()

# Scatter trace 추가
fig.add_trace(go.Scatter(x=x, y=y, mode='markers'))

# 테이블 생성
data = {'x': x, 'y': y}
df = pd.DataFrame(data)
table = go.Table(header=dict(values=list(df.columns)),
                 cells=dict(values=[df[col] for col in df.columns]))

# 차트와 테이블을 하나의 subplot에 배치
fig = make_subplots(rows=1, cols=2, column_widths=[0.7, 0.3],
                    subplot_titles=['Scatter Plot', 'Selected Data'],
                    specs=[[{"type": "scatter"}, {"type": "table"}]])
fig.add_trace(go.Scatter(x=x, y=y, mode='markers'), row=1, col=1)
fig.add_trace(table, row=1, col=2)


# 이벤트 핸들러 함수
def handle_click(trace, points, state):
    print("111")
    # 선택한 항목의 인덱스 가져오기
    selected_indices = [point['pointIndex'] for point in points]
    print(selected_indices);

    # 선택한 항목에 대한 정보 업데이트
    selected_data = df.iloc[selected_indices]
    state['data'] = selected_data

    # 테이블 업데이트
    table_cells = [selected_data[col] for col in selected_data.columns]
    table_cells.insert(0, selected_data.columns)
    table.data[0].cells.values = table_cells


# 이벤트 핸들러 함수
def handle_select(trace, points, state):
    print("kk")

# 이벤트 핸들러 추가
fig.data[0].on_click(handle_click, {'data': None})
fig.data[0].on_selection(handle_select, {'data': None})

# 레이아웃 업데이트
fig.update_layout(
    title="Select items to see the table",
)

##### -->



##### <<--

# 차트와 테이블 표시
fig.show()

'''
# [1] 안 됨
# 줌 이벤트 핸들러 함수
def handle_relayout(fig, state):
    # x, y축의 range 가져오기
    x_range = fig['layout']['xaxis']['range']
    y_range = fig['layout']['yaxis']['range']

    # 선택된 데이터가 있는 경우 테이블 업데이트
    if state['data'] is not None:
        # 선택된 데이터에서 x, y축 범위 내에 있는 데이터만 추출
        selected_data = state['data'].loc[(state['data']['x'] >= x_range[0]) &
                                          (state['data']['x'] <= x_range[1]) &
                                          (state['data']['y'] >= y_range[0]) &
                                          (state['data']['y'] <= y_range[1])]
        table_cells = [selected_data[col] for col in selected_data.columns]
        table_cells.insert(0, selected_data.columns)
        table.data[0].cells.values = table_cells


# 줌 이벤트 핸들러 추가
fig.add_event_listener('plotly_relayout', lambda event, fig: handle_relayout(fig, state))

# state 객체 초기화
state = {'data': None}
'''

'''
# [2] 안 됨
fig.update_layout(
    title="Select items to see the table",
    xaxis={
        "range": [0, 6],
        "fixedrange": True
    },
    yaxis={
        "range": [9, 15],
        "fixedrange": True
    }
)

# 줌 이벤트 핸들러 추가
def handle_relayout(fig, trace, state):
    # x, y축의 range 가져오기
    x_range = fig['layout']['xaxis']['range']
    y_range = fig['layout']['yaxis']['range']

    # 선택된 데이터가 있는 경우 테이블 업데이트
    if state['data'] is not None:
        # 선택된 데이터에서 x, y축 범위 내에 있는 데이터만 추출
        selected_data = state['data'].loc[(state['data']['x'] >= x_range[0]) &
                                          (state['data']['x'] <= x_range[1]) &
                                          (state['data']['y'] >= y_range[0]) &
                                          (state['data']['y'] <= y_range[1])]
        table_cells = [selected_data[col] for col in selected_data.columns]
        table_cells.insert(0, selected_data.columns)
        table.data[0].cells.values = table_cells

fig.update_layout(
    {"dragmode": "select"},
    annotations=[
        {
            "text": "Drag to select points",
            "showarrow": False,
            "x": 0.5,
            "y": 1.1,
            "xref": "paper",
            "yref": "paper",
            "font": {"size": 14}
        }
    ]
)

# 이벤트 핸들러 추가
fig.data[0].on_click(lambda trace, points, state: handle_click(trace, points, state))
fig.update_layout(
    {"clickmode": "event+select"}
)

# 줌 이벤트 핸들러 추가
fig.update_layout(
    {"dragmode": "zoom"},
    {"uirevision": "no reset of zoom"},
    xaxis={
        "fixedrange": True
    },
    yaxis={
        "fixedrange": True
    }
)
fig.update_xaxes({"range[0]": 0, "range[1]": 6})
fig.update_yaxes({"range[0]": 9, "range[1]": 15})

fig.update_layout(
    {"plot_bgcolor": "#F9F9F9", "paper_bgcolor": "#F9F9F9"}
)

# state 객체 초기화
state = {'data': None}
'''