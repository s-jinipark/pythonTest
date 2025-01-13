'''
157 현재 시간을 년-월-일 시:분:초로 출력하기(localtime, strftime)
158 올해 경과된 날짜수 계산하기(localtime)
159 오늘의 요일 계산하기(localtime)
160 프로그램 실행 시간 계산하기(datetimenow)
161 주어진 숫자를 천 단위로 구분하기
162 문자열의 각 문자를 그 다음 문자로 변경하기
163 URL에서 호스트 도메인 추출하기
164 URL에서 쿼리 문자열 추출하기
165 스택 구현하기(append, pop)
166 문장에 나타나는 문자 빈도수 계산하기
167 텍스트 파일에 있는 단어 개수 계산하기
168 파일에서 특정 단어 개수 계산하기
169 파일에서 특정 문자열 교체하기
170 URL에 접속하여 HTML 페이지 화면에 출력하기
171 URL에 접속하여 HTML 페이지를 파일로 저장하기
172 인터넷에 있는 이미지를 내 PC로 저장하기
173 인터넷에 있는 대용량 파일을 내 PC로 저장하기
174 10MB 파일을 1MB 파일 10개로 분리하기
175 1MB 파일 10개를 합쳐서 10MB 파일로 만들기
176 파일을 ZIP 압축 파일로 만들기
177 디렉터리를 하나의 ZIP 압축 파일로 만들기
178 ZIP 파일 압축 풀기
179 로또 번호 추출기 만들기
180 남녀 파트너 정해주기 프로그램 만들기(zip)
'''

print("-----------------------------------")
print("157 현재 시간을 년-월-일 시:분:초로 출력하기(localtime, strftime)")
from time import localtime, strftime
logfile = 'test.log'

def writelog(logfile, log) :
    time_stamp = strftime('%Y-%m-%d %X\t', localtime())
    log = time_stamp + log + '\n'

    with open (logfile, 'a') as f:
        f.writelines(log)

writelog(logfile, '첫번째 로깅 문장')

# FileNotFoundError: [Errno 2] No such file or directory: 'test.log'
# 파일 만들어 놓고 수행
# 예 > 2022-01-22 14:32:58	첫번째 로깅 문장
'''
포멧문자열      설명
%Y          년도
%m          월
%d          일
%H          시간 24
%M          분
%S          초
%x          현재 날짜를 월/일/년 으로 나타냄. 예> 01/21/22 (22년 1월 21일)
%X          현재 시간을 시:분:초 로 나타냄. 예> 22:10:15
'''


print("-----------------------------------")
print("158 올해 경과된 날짜수 계산하기(localtime)")
from time import localtime

t = localtime()
start_day = '%d-01-01'%t.tm_year
elapsed_day = t.tm_yday   # 해당 년도의 1월 1일 부터 현재 날짜까지 경과된 날짜 수

print('오늘은 [%s] 이후 [%d] 일 째 되는 날입니다.'%(start_day, elapsed_day))


print("-----------------------------------")
print("159 오늘의 요일 계산하기(localtime)")
#from time import localtime

weekdays = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일' ]
t = localtime()
today = '%d-%d-%d'%(t.tm_year, t.tm_mon, t.tm_mday)
week = weekdays[t.tm_wday]

print('[%s] 오늘은 [%s] 입니다. '%(today, week))   # 0 이면 월요일 !


print("-----------------------------------")
print("160 프로그램 실행 시간 계산하기(datetimenow)")
from datetime import datetime

start = datetime.now()
print('1에서 백만까지 더합니다')
ret = 0
for i in range(1000001):
    ret += i

print('더한 결과 : %d'%ret)
end = datetime.now()

elapsed = end - start
print('총 계산 시간 : ', end='' ); print(elapsed)
elapsed_ms = int(elapsed.total_seconds()*1000)
print('총 계산 시간 : %d ms'%elapsed_ms)


print("-----------------------------------")
print("161 주어진 숫자를 천 단위로 구분하기")
num = '7943785405904'

if num.isdigit():
    print('숫자')
    num = num[::-1]
    print(num)  # reverse 로 한 뒤 앞에서 부터
    ret = ''
    for i, c in enumerate(num):
        i += 1
        if i != len(num) and i % 3 == 0 :
            ret += (c + ',')
        else :
            ret += c
    print(ret)
    ret = ret[::-1]  # 다시 역순으로 ..
    print(ret)
else :
    print('숫자 아님')

'''
숫자로만 구성된 문자열이면 사용자 입력 숫자를 거꾸로 배열
이유는 주어진 수의 일의 자리부터 세자리씩 끊어 콤마로 구분 
나중에 본래 순서로 되돌리는 것이
 => 구현에 편리
'''


print("-----------------------------------")
print("162 문자열의 각 문자를 그 다음 문자로 변경하기")
text = '안녕하세요. 홍길동입니다.'
ret = ''
for i in range(len(text)) :
    if i != len(text)-1 :
        ret += text[i+1]
    else :
        ret += text[0]

print(ret)
'''
결과>
녕하세요. 홍길동입니다.안

i 가 맨마지막이 아니면 i+1 을 붙이고
마자막이면 index 0 의 값을 붙임

=> ?? 어디에 쓰일지 모르겠음 ??
'''


print("-----------------------------------")
print("163 URL에서 호스트 도메인 추출하기")
url = 'http://www.naver.com/main/read.nhn?mode=LSD&mid=shm'

tmp = url.split('/')
domain = tmp[2]
print(domain)


print("-----------------------------------")
print("164 URL에서 쿼리 문자열 추출하기")
url = 'http://www.naver.com/main/read.nhn?mode=LSD&mid=shm'

tmp = url.split('?')
queries = tmp[1].split('&')
for query in queries :
    print(query)


print("-----------------------------------")
print("165 스택 구현하기(append, pop)")
mystack = []

def putdata(data):
    global mystack
    mystack.append(data)

def popdata():
    global mystack
    if len(mystack) == 0 :
        return None
    return mystack.pop()

putdata('데이터1')
putdata([3,4,5,6])
putdata(12345)

print('<스택상태>: ', end=''); print(mystack)

ret = popdata()
while ret != None :
    print('스택에서 데이터 추출 : ', end=''); print(ret)
    print('<스택상태>: ', end=''); print(mystack)
    ret = popdata()


print("-----------------------------------")
print("166 문장에 나타나는 문자 빈도수 계산하기")
def getTextFreq(filename) :
    with open(filename, 'r') as f :
        text = f.read()
        fa = {}   # 빈 사전 , 문자:빈도수 가 요소인 사전
        for c in text:
            if c in fa :
                fa[c] += 1
            else :
                fa[c] = 1
    return fa

ret = getTextFreq('mydata.txt')
ret = sorted(ret.items(), key=lambda x : x[1], reverse=True)  # 예제 131 참조
for c, freq in ret :
    if c == '\n' :
        continue
    print('[%c] -> [%d] 회 나타남'%(c, freq))
'''
# if c == '\n' : 이 부분이 없다면 
아래가 출력됨
[
] -> [43] 회 나타남
'''

print("-----------------------------------")
print("167 텍스트 파일에 있는 단어 개수 계산하기")
with open('mydata.txt', 'r') as f:
    data = f.read()
    tmp = data.split()
    print('단어수 : [%d]'%len(tmp))


print("-----------------------------------")
print("168 파일에서 특정 단어 개수 계산하기")
def countWord(filename, word) :
    with open(filename, 'r') as f:
        text = f.read()
        text = text.lower()
        pos = text.find(word)   # find 는 092 참조
        count = 0
        while pos != -1 :
            count += 1
            pos = text.find(word, pos+1)  # 찾은 word의 위치 다음부터...
    return count

word = 'too'
word = word.lower()
ret = countWord('mydata.txt', word)
print('[%s] 의 개수 : %d'%(word, ret))


print("-----------------------------------")
print("169 파일에서 특정 문자열 교체하기")
t1 = 'too'   # 찾을 단어
t2 = 'tmi'   # 변경할 단어

with open('mydata.txt', 'r') as f :
    with open('mydata2.txt', 'w') as h :
        text = f.read()
        text = text.replace(t1, t2)
        h.write(text)

print('[%s] 를 [%s] 로 변경하였습니다.'%(t1, t2))


print("-----------------------------------")
print("170 URL에 접속하여 HTML 페이지 화면에 출력하기")
from urllib.request import urlopen

url = 'https://www.python.org'
with urlopen(url) as f:
    doc = f.read().decode()
    #print(doc)

'''
urllib.request 모듈의 urlopen() 을 임포트합니다.
urlopen(url) 은 url 에 접속하여 파일처럼 다룰 수 있는 핸들을 리턴합니다.

with urlopen(url) as f:
  # url 에 접속하여 오픈하고 그 핸들을 f 로 둡니다
f.read() 는 url 로 부터 해당 리소스 데이터를 바이트 스트림으로 읽어옵니다
f.read().decode() 로 텍스트로 변환
(엄밀히 말하면 유니코드 문자열)
'''


print("-----------------------------------")
print("171 URL에 접속하여 HTML 페이지를 파일로 저장하기")
#from urllib.request import urlopen

url = 'https://www.python.org'
with urlopen(url) as f :
    doc = f.read().decode()
    with open('python_home.html', 'w', encoding='UTF-8') as h:
        h.writelines(doc)

# UnicodeEncodeError: 'cp949' codec can't encode character '\U0001f389' in position 0: illegal multibyte sequence
# 오류나서  파일 저장 시  encoding='UTF-8'  (추가)


print("-----------------------------------")
print("172 인터넷에 있는 이미지를 내 PC로 저장하기")
#from urllib.request import urlopen

imgurl = 'http://www.infopub.co.kr/l_pic/07000080.jpg'
imgname = imgurl.split('/')[-1]

try :
    with urlopen(imgurl) as f:
        with open(imgname, 'wb') as h :
            img = f.read()
            h.write(img)
except Exception as e :
    print(e)


print("-----------------------------------")
print("173 인터넷에 있는 대용량 파일을 내 PC로 저장하기")
#from urllib.request import urlopen

BUFSIZE = 256 * 1024

fileurl = 'http://www.python.org/ftp/python/3.7.2/python-3.7.2.exe'
filename = fileurl.split('/')[-1]

try :
    with urlopen(fileurl) as f :
        with open(filename, 'wb') as h :   # 파일 핸들을 f,  h 로 둠
            buf = f.read(BUFSIZE)
            while buf :
                h.write(buf)
                buf = f.read(BUFSIZE)
except Exception as e :
    print(e)
'''
먼저 fileurl 을 BUFSIZE 만큼 읽어 buf 로 지정하고 while 문으로 진입합니다.
로컬 파일인 filename 에 buf 로 지정된 데이터를 저장하고,
fileurl 에서 다시 BUFSIZE 만큼 읽고 buf 로 두는 반복을 buf 에 데이터가 담기지 않을 때까지 계속 수행
'''

print("-----------------------------------")
#print("174 10MB 파일을 1MB 파일 10개로 분리하기")
print("174 25MB 파일을 5MB 파일 5개로 분리하기")
filename = 'python-3.7.2.exe'
subsize = 1024*1024*5  # 5MB
suffix = 0

with open(filename, 'rb') as f :
    buf = f.read(subsize)
    while buf :
        subfilename = filename + '_' + str(suffix)
        with open(subfilename, 'wb') as h:
            h.write(buf)
            print('[%s] 완료'%subfilename)
        buf = f.read(subsize)
        suffix += 1


print("-----------------------------------")
#print("175 1MB 파일 10개를 합쳐서 10MB 파일로 만들기")
print("175 5MB 파일 5개를 합쳐서 25MB 파일로 만들기")
BUFSIZE = 256*1024
merge_filename = 'ret.exe'
filelist = ['python-3.7.2.exe_'+ str(x) for x in range(5)]
#print(filelist)

with open(merge_filename, 'wb') as f :
    for filename in filelist :
        print('[%s] 합치는 중 ..'%filename)
        with open(filename, 'rb') as h:
            buf = h.read(BUFSIZE)
            while buf :
                f.write(buf)
                buf = h.read(BUFSIZE)
print('파일 합치기 완료')


print("-----------------------------------")
print("176 파일을 ZIP 압축 파일로 만들기")
from zipfile import *

def compressZip(zipname, filename) :
    print('[%s] -> [%s] 압축 ... '%(filename, zipname))
    with ZipFile(zipname, 'w') as ziph :
        ziph.write(filename)

    print('압축이 끝났습니다.')

filename = 'mydata.txt'
zipname = filename + '.zip'
compressZip(zipname, filename)

'''
ZIP 파일을 기록하려면 ZipFile 객체를 쓰기 모드로 생성해야 합니다.
파일을 쓰기 모드로 오픈하는 것과 비슷하지만 
압축 알고리즘을 구동해야 하므로 일반적인 파일을 오픈하는 것과는 달리 ZipFile 객체를 이용
'''

print("-----------------------------------")
print("177 디렉터리를 하나의 ZIP 압축 파일로 만들기")
#from zipfile import *
import os

def compressAll(zipname, folder) :
    print('[%s] -> [%s] 압축 ... '%(folder, zipname))
    with ZipFile(zipname, 'w') as ziph :
        for dirname, subdirs, files in os.walk(folder) :
            for file in files :
                ziph.write(os.path.join(dirname, file))

folder = 'temp'
zipname = folder + '_2.zip'
compressAll(zipname, folder)

'''
tmmp
 ├─ tmp2  ┬─ file4
 ├─ tmp3  └  file5
 ├ file1
 ├ file2 
 └ file3

walk(tmp) 의 리턴
[ ('tmp', ['tmp2', 'tmp3'], ['file1', 'file2', 'file3']) , 
  ('tmp/tmp2', [], ['file4', 'file5']) ,
  ('tmp/tmp3' [], [] )
]  
'''


print("-----------------------------------")
print("178 ZIP 파일 압축 풀기")
#from zipfile import *

def extractZip(zipname) :
    with ZipFile(zipname, 'r') as ziph :
        ziph.extractall()
        print('[%s] 가 성공적으로 추출되었습니다.'%zipname)

os.chdir('temp4')
extractZip('../temp_2.zip')
os.chdir('..')


print("-----------------------------------")
print("179 로또 번호 추출기 만들기")
from random import shuffle
from time import sleep

game_num = 4

for i in range(game_num) :
    balls = [x+1 for x in range(45)]
    ret = []
    for j in range(6) :
        shuffle(balls)
        number = balls.pop()
        ret.append(number)
    ret.sort()
    print('로또 번호 [%d]'%(i+1), end='')
    print(ret)
    sleep(1)


print("-----------------------------------")
print("180 남녀 파트너 정해주기 프로그램 만들기(zip)")
#from random import shuffle

male = ['수퍼맨', '심봉사', '로미오', '이몽룡', '마루치']
female = ['원더우면', '뺑덕', '줄리엣', '성춘향', '아라치']

shuffle(male)
shuffle(female)

couples = zip(male, female)

for i , couple in enumerate(couples) :
    print('커플 %d  : [%s] - [%s]'%(i+1, couple[0], couple[1]))

'''
파이썬 내장함수 zip() 은 동일한 요소 개수를 가진 두개 이상의 리스트를 인자로 받고,
각 리스트의 같은 인덱스끼리 묶은 튜플을 요소로 하는 리스트로 만들어 리턴
예를 들어 zip([1,2,3], [5,6,7]) 은 [(1,5), (2,6), (3,7)]
zip([1,3], [5,6], [8,9])  => [(1,5,8), (3,6,9)] 
'''