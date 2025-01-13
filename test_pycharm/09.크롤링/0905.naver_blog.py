import requests
from bs4 import BeautifulSoup
import urllib
import json

query = "python"
#query = "파이썬강좌"
#query = urllib.parse.quote(query)  # 오류가 발생해서
print(query)
# => UnicodeEncodeError: 'latin-1' codec can't encode characters in position 92-96: ordinal not in range(256)

#url = "https://section.blog.naver.com/Search/Post.naver?pageNo=1&rangeType=ALL&orderBy=sim&keyword={}".format(query)

# 2020-11-29 일 수정
# 웹페이지를 호출하면 아래의 주소로 ajax 통신을 하여 결과를 받아온 후 결과를 렌더링 하는 형태로 변경됨.
#url = "https://s.search.naver.com/p/blog/search.naver?where=blog&sm=tab_pge&api_type=1&query={}&start={}".format(keyword, start_page)

# 2021-12-15 현재
current_page = 1

url = "https://section.blog.naver.com/ajax/SearchList.naver?countPerPage=7&currentPage={}&endDate=&keyword={}&orderBy=sim&startDate=&type=".format(current_page, query)

# 오류남
# => {"result":{"code":"csrf","message":"잘못된 요청입니다"}}

# 요청시 헤더정보를 크롬으로 지정
request_headers = {
'User-Agent' : ('Mozilla/5.0 (Windows NT 10.0;Win64; x64)\
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98\
Safari/537.36') }

#r = requests.get(url)
#r = requests.get(url,headers = request_headers)
# => 안됨

# (참조) https://cceeddcc.tistory.com/5
headers = {'Referer': 'https://section.blog.naver.com/Search/Post.naver?pageNo={}&rangeType=ALL&orderBy=sim&keyword={}'.format(str(current_page), query)}
#headers = {'Referer': 'https://section.blog.naver.com/Search/Post.naver?pageNo=' + str(current_page) +'&rangeType=ALL&orderBy=sim&keyword=' +  query }
r = requests.get(url, headers = headers)

#bs = BeautifulSoup(r.text, "lxml")
bs = BeautifulSoup(r.text, "html.parser")

print(bs)
print(type(bs))
#d = json.loads(str(bs))
# json 데이터에서 "searchList" 항목의 값을 추출
#print(d['result']['searchList'])


#####
# 보완 필요
