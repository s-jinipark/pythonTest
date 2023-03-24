# Seaborn 패키지 불러오기
import seaborn as sns

# 샘플 데이터셋 목록 확인하기
print(sns.get_dataset_names() )


diamonds = sns.load_dataset('diamonds') # 다이아몬드 데이터셋
print( diamonds.head() )


import plotly.express as px

# 선거 데이터 불러오기
election = px.data.election()
print( election.head() )

