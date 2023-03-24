import plotly.express as px
import pandas as pd

# 데이터 불러오기
#df = px.data.iris()

# 엑셀  파일을 dataframe으로 변경
#df = pd.read_excel("ch06-01-test-2.xlsx", engine = "openpyxl")

# df = pd.read_excel(r"C:\Users\LGCNS\Desktop\웹전표\로그\0201-AP\0201_ap1_test.xlsx",
#                    engine = "openpyxl",  sheet_name="0201_ap1_test")

# [2]
df = pd.read_excel(r"C:\Users\LGCNS\Desktop\웹전표\로그\0201_batch_test.xlsx",
                   engine = "openpyxl",  sheet_name="0201_batch_test")

# [3]
# df = pd.read_excel(r"C:\Users\LGCNS\Desktop\웹전표\로그\0222-ap1\0222_ap1_test.xlsx",
#                    engine = "openpyxl",  sheet_name="0222_ap1_test")

print(df)

# 기본
#fig = px.scatter(data_frame=df, x="END TIME", y="TAKE TIME")

#fig = px.scatter(data_frame=df, x="END TIME", y="TAKE TIME", color="I/F ID")
fig = px.scatter(data_frame=df, x="END TIME", y="TAKE TIME", color="tgt_name")


# [2]
# 축 범위 지정
#fig.update_xaxes(range=[0, 5])
fig.update_xaxes(range=['2023-02-01T16:00:00.445945','2023-02-01T19:00:12.026876'])
#fig.update_yaxes(range=[0, 210000])
fig.update_yaxes(range=[0, 35000])

fig.show()
