import requests
from bs4 import BeautifulSoup
import time
import json

lasttime = int(round(time.time() * 1000))

print(lasttime)

#r = requests.get("https://dable-public.s3-ap-northeast-1.amazonaws.com/static/production/tmp/media-index/search_word.json?v=1639471079346")
r = requests.get("https://dable-public.s3-ap-northeast-1.amazonaws.com/static/production/tmp/media-index/search_word.json?v=" + str(lasttime) )

bs = BeautifulSoup(r.text, "html.parser")

print(bs)
d = json.loads(str(bs))

# json 데이터에서 "data" 항목의 값을 추출
ranks = d.get("data")

print(ranks)

# 해당 값은 리스트 형태로 제공되기에 리스트만큼 반복
for r in ranks:
    # 각 데이터는 rank, keyword, keyword_synomyms
    rank = r.get("rank")
    keyword = r.get("keyword")
    print(rank, keyword)

# https://kdx.kr/m/service/searchtrend/view
# 한국 데이터 거래소
