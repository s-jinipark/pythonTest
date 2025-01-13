'''
039 함수 이해하기(def)
040 함수 인자 이해하기
041 지역변수와 전역변수 이해하기(global)
042 함수 리턴값 이해하기(return)
043 파이썬 모듈 이해하기
044 파이썬 패키지 이해하기
045 파이썬 모듈 임포트 이해하기 ① (import)
046 파이썬 모듈 임포트 이해하기 ② (from~import)
047 파이썬 모듈 임포트 이해하기 ③ (import~as)
048 파일 열고 닫기(open, close)
'''

##################################################
print("039 함수 이해하기(def)")
def add_number(n1, n2) :
    ret = n1 + n2
    return ret
def add_text(t1, t2):
    print(t1+t2)

ans = add_number(10,15)
print(ans)
text1 = '대한민국 ~ '
text2 = '만세 !!'
add_text(text1, text2)


##################################################
print("040 함수 인자 이해하기")
def add_text(t1, t2='파이썬'):
    print(t1 + ' : ' + t2)

add_text('베스트')
add_text(t2='대한민국', t1='1등')

def func1(*args) :
    print(args)

def func2(width, height, **kwargs):
    print(kwargs)

func1()
func1(3,5,1,5)
func2(10,20)
func2(10,20, depth=50, color='blue')  # 키워드 인자
# {'depth': 50, 'color': 'blue'} 이 출력됨


##################################################
print("041 지역변수와 전역변수 이해하기(global)")
param = 10
strdata = '전역변수'

def func1():
    strdata = '지역변수'
    print(strdata)

def func2(param):
    param = 1

def func3():
    global param
    param = 50

func1()
print(strdata)
print(param)  # 10 이 출력됨
func2(param)
print(param)  # 10 이 출력됨(동일)
func3()
print(param)  # 50 이 출력됨


##################################################
print("042 함수 리턴값 이해하기(return)")
def reverse(x, y, z):
    return z, y, x

ret = reverse(1,2,3)
print(ret)

r1, r2, r3 = reverse('a', 'b', 'c')
print(r1);print(r2);print(r3)


##################################################
print("043 파이썬 모듈 이해하기")
import time

print('5초간 프로그램을 정지합니다.')
#time.sleep(5)
print('5초가 지나갔습니다.')

'''
코드를 작성할 때 이미 만들어져 있는 함수를 활용하면 보다 효율적이고 빠르게 개발
이미 만들어져 있고 안정성이 검증된 함수들을 성격에 맞게 하나의 파이썬 파일에 묶어 만들어 놓은 것을 "모듈" 이라 부름

파이썬 모듈을 만드는 방법
----- mylib.py -----
def add_text(t1, t2) :
    return t1 + ' : ' + t2

def reverse(x, y, z) :
    return z, y, x

구현 프로그램에 다음과 같이 mylib 을 임포트
import mylib

ret1 = mylib.add_text('대한민국', '1등')
print(ret1)

'''


##################################################
print("044 파이썬 패키지 이해하기")
'''
import mypackage.mylib

ret1 = mypackage.mylib.add_text('대한민국', '1등')

=>
파이썬 모듈을 계층적인 디렉터리 형태로 구성한 것을 파이썬 패키지라 합니다

1. mypackage 라는 이름의 디렉터리를 만듬
2. mypackage 디렉터리로 이동
3. 앞의 mylib.py 를 mypackage 디렉터리로 복사
4. mypackage 폴더에 version=1.0 이 내용인 __init__.py 파일 생성
5. 서브 디렉터리를 생성한 후 하위 패키지를 구성하려면
   1~4 과정을 동일하게 반복
    
'''


##################################################
print("046 파이썬 모듈 임포트 이해하기 ② (from~import)")

from time import sleep

sleep(1)

'''
from 모듈이름 import 함수이름
from 패키지이름 import 모듈이름
'''


##################################################
print("047 파이썬 모듈 임포트 이해하기 ③ (import~as)")
'''
import mypackage as mp
ret1 = mp.mylib.add_text('대한민국', '1등')

이름이 긴 모듈이나 계층구조가 복잡한 모듈인 경우,
별명을 붙여 간단하게 호출할 수 있음

import 이름이 긴 모듈명 as 별명

'''


##################################################
print("048 파일 열고 닫기(open, close)")

'''
f1 = open('text.txt', 'r')
  ...
f1.close()

open(파일이름, 모드)
모드는
r 또는 rt         텍스트 모드로 읽기
w 또는 wt         텍스트 모드로 쓰기
a 또는 at         텍스트 모드로 파일 마지막에 추가하기
rb              바이너리 모드로 읽기
wb              바이너리 모드로 쓰기
ab              바이너리 모드로 파일 마지막에 추가하기
'''


