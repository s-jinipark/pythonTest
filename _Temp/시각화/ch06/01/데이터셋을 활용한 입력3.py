import plotly.graph_objects as go

# 데이터 생성
x = [1, 2, 3, 4, 5]
y = [10, 11, 12, 13, 14]

# Figure 객체 생성
fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=y, mode='markers'))


# 이벤트 핸들러 함수
def handle_click(trace, points, state):
    # 선택한 항목의 인덱스 가져오기
    selected_indices = [point['pointIndex'] for point in points]

    # 선택한 항목에 대한 목록 업데이트
    selected_values = [y[i] for i in selected_indices]
    state['text'] = f"Selected values: {selected_values}"


# 이벤트 핸들러 추가
fig.data[0].on_click(handle_click, {'text': ''})

# 레이아웃 업데이트
fig.update_layout(
    title="Select items to see the list",
    annotations=[dict(
        text="",
        x=0.5,
        y=1.1,
        showarrow=False,
        font=dict(size=16)
    )]
)

# 차트 표시
fig.show()

''''
chatGPT 의 답변임
'''