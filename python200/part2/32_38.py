'''
032 멤버체크 이해하기(in)
033 문자열 이해하기
034 문자열 포맷팅 이해하기
035 이스케이프 문자 이해하기
036 리스트 이해하기([ ])
037 튜플 이해하기(( ))
038 사전 이해하기({ })

'''

##################################################
print("032 멤버체크 이해하기(in)")
listdata = [1,2,3,4]
ret1 = 5 in listdata
ret2 = 4 in listdata
print(ret1)
print(ret2)
strdata = 'abcde'
ret3 = 'c' in strdata
ret4 = 'l' in strdata
print(ret3)
print(ret4)


##################################################
print("033 문자열 이해하기")
strdata1 = '나는 파이썬 프로그래머다'
strdata2 = 'You are a programmer'
strdata3 = """I love
    python.  You love
python too !
"""
strdata4 = "My son's name is John"
strdata5 = '문자열 "abc" 의 길이는 3 입니다'

print(strdata1)
print(strdata2)
print(strdata3)
print(strdata4)  # "" 안에서 ' 사용하기
print(strdata5)  # '' 안에서 " 사용하기


##################################################
print("034 문자열 포맷팅 이해하기")
txt1 = '자바'; txt2 = '파이썬'
num1 = 5 ; num2 = 10
print('나는 %s 보다 %s 에 더 익숙합니다.'%(txt1, txt2))
print('%s 는 %s 보다 %d 배 더 쉽습니다.'%(txt2, txt1, num1))
print('%d + %d = %d'%(num1, num2, num1+num2))
print("=====")
# from time import sleep
# for i in range(100):
#     msg = '\r진행률 %d %%'%(i+1)
#     print(' '*len(msg), end='')
#     print(msg, end='')
#     sleep(0.1)


##################################################
print("035 이스케이프 문자 이해하기")
print('나는 파이썬을 사랑합니다.\n파이썬은 자바보다 훨씬 쉽습니다.')
print('이 문장은 화면폭에 비해 ... \
      다음줄에 연속')
      # print 하면 한줄, 화면에서


##################################################
print("036 리스트 이해하기([ ])")
list1 = [1,2,3,4,5]
list2 = ['a', 'b', 'c']
list3 = [1, 'a', 'abc', [1,2,3,4,5], ['a','b','c']]
list1[0] = 6
print(list1)

def myfunc():
    print('안녕하세요(myfunc)')
list4 = [1,2, myfunc]
list4[2]()  # ?? '안녕하세요...' 출력됨 [실제 사용될지는 .. 글쎄]


##################################################
print("037 튜플 이해하기(( ))")
tuple1 = (1,2,3,4,5)
tuple2 = ('a', 'b', 'c')
tuple3 = (1, 'a', 'abc', [1,2,3,4,5], ['a', 'b', 'c'])
#tuple1[0] = 6
  # (오류 발생) TypeError: 'tuple' object does not support item assignment

def myfunc37():
    print('안녕하세요(37)')
tuple4 = (1,2, myfunc37)
tuple4[2]()  # ?? '안녕하세요...' 출력됨 [실제 사용될지는 .. 글쎄]


##################################################
print("038 사전 이해하기({ })")

dict1 = {'a':1, 'b':2, 'c':3}
print(dict1['a'])  # dict[a] 로 하면 오류남 NameError: name 'a' is not defined
dict1['d'] = 4  # 새로운 키:값 추가
print(dict1)
dict1['b'] = 7
print(dict1)
print(len(dict1))  # 4 가 출력됨


