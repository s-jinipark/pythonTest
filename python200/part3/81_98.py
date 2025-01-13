'''
081 문자열에서 특정 문자가 있는지 확인하기(in)
082 문자열에서 특정 문자열이 있는지 확인하기(in)
083 문자열 길이 구하기(len)
084 문자열이 알파벳인지 검사하기(isalpha)
085 문자열이 숫자인지 검사하기(isdigit)
086 문자열이 알파벳 또는 숫자인지 검사하기(isalnum)
087 문자열에서 대소문자 변환하기(upper, lower)
088 문자열에서 좌우 공백 제거하기(lstrip, rstrip, strip)
089 문자열을 수치형 자료로 변환하기(int, float)
090 수치형 자료를 문자열로 변환하기(str)
091 문자열에 있는 문자(열) 개수 구하기(count)
092 문자열에서 특정 문자(열) 위치 찾기(find)
093 문자열을 특정 문자(열)로 분리하기(split)
094 문자열을 특정 문자(열)로 결합하기(join)
095 문자열에서 특정 문자(열)를 다른 문자(열)로 바꾸기(replace)
096 문자열을 바이트 객체로 바꾸기(encode)
097 바이트 객체를 문자열로 바꾸기(decode)
098 문자열을 정렬하기(sorted, join)
'''

print("-----------------------------------")
print("081 문자열에서 특정 문자가 있는지 확인하기(in)")
#msg = input("임의의 문장을 입력하시오")
msg = 'a beutiful day'
if 'a' in msg :
    print("당신이 입력한 문장에는 a 가 있습니다")
else:
    print("당신이 입력한 문장에는 a 가 없습니다")


print("-----------------------------------")
print("082 문자열에서 특정 문자열이 있는지 확인하기(in)")
msg = 'This is a beutiful day'
if 'is' in msg:
    print("당신이 입력한 문장에는 'is' 가 있습니다")
else:
    print("당신이 입력한 문장에는 'is' 가 없습니다")


print("-----------------------------------")
print("083 문자열 길이 구하기(len)")
msg = 'Python 파이썬'
msglen = len(msg)
print('문장의 길이는 <%d> 입니다.'%msglen)  # 10
msglen = len(msg.encode())
print('문장의 길이는 <%d> 입니다.'%msglen)  # 16 (파이썬 => 9 바이트 처리)


print("-----------------------------------")
print("084 문자열이 알파벳인지 검사하기(isalpha)")
txt1 = 'A'
txt2 = '안녕'
txt3 = 'Warcraft Three'
txt4 = '3PO'
ret1 = txt1.isalpha()
ret2 = txt2.isalpha()
ret3 = txt3.isalpha()
ret4 = txt4.isalpha()
print(ret1)  # True
print(ret2)  # True
print(ret3)  # False (공백 포함)
print(ret4)  # False (숫자 3 포함)
'''
문자열의 모든 요소가 알파벳이나 한글과 같은 언어 문자인지 판단하는 방법
=> 사람의 언어를 표현하기 위해 사용되는 문자로만 구성되어 있는지
'''

print("-----------------------------------")
print("085 문자열이 숫자인지 검사하기(isdigit)")
txt1 = '010-2439-9090'
txt2 = 'R2D2'
txt3 = '1212'
ret1 = txt1.isdigit()
ret2 = txt2.isdigit()
ret3 = txt3.isdigit()
print(ret1)  # False
print(ret2)  # False
print(ret3)  # True


print("-----------------------------------")
print("086 문자열이 알파벳 또는 숫자인지 검사하기(isalnum)")
txt1 = '안녕하세요?'
txt2 = '1.Title-제목'
txt3 = '3피오R2D2'
ret1 = txt1.isalnum()
ret2 = txt2.isalnum()
ret3 = txt3.isalnum()
print(ret1)  # False  (? )
print(ret2)  # False  (- )
print(ret3)  # True


print("-----------------------------------")
print("087 문자열에서 대소문자 변환하기(upper, lower)")
txt = 'A lot of Things occur each day.'
ret1 = txt.upper()
ret2 = txt.lower()
print(ret1)
print(ret2)


print("-----------------------------------")
print("088 문자열에서 좌우 공백 제거하기(lstrip, rstrip, strip)")
txt = '  양쪽에 공백이 있음.  '
ret1 = txt.lstrip()
ret2 = txt.rstrip()
ret3 = txt.strip()
print('<' + txt + '>')
print('<' + ret1 + '>')
print('<' + ret2 + '>')
print('<' + ret3 + '>')


print("-----------------------------------")
print("089 문자열을 수치형 자료로 변환하기(int, float)")
#numstr = input("숫자를 입력하세요")
numstr = 4
try :
    num = int(numstr)
    print('입력한 숫자는 정수<%d>'%num)
except :
    try :
        num = float(numstr)
        print('입력한 숫자는 실수<%f>'%num)
    except :
        print('++ 숫자를 입력하세요 ++')

'''
숫자를 입력하세요4.5
입력한 숫자는 실수<4.500000>

숫자를 입력하세요AAA
++ 숫자를 입력하세요 ++

'''
print("-----------------------------------")
print("090 수치형 자료를 문자열로 변환하기(str)")
num1 = 1234
num2 = 3.14

numstr1 = str(num1)
numstr2 = str(num2)
print('num1 을 문자열로 변환한 값은 "%s" 입니다'%numstr1)
print('num2 을 문자열로 변환한 값은 "%s" 입니다'%numstr2)


print("-----------------------------------")
print("091 문자열에 있는 문자(열) 개수 구하기(count)")
txt = 'A lot of Things occur each day, every day.'
word_count1 = txt.count('o')
word_count2 = txt.count('day')
word_count3 = txt.count(' ')
print(word_count1)
print(word_count2)
print(word_count3)  # 8  (공백은 보통 단어를 구분하는 기호로 사용되므로
                    #     공백개수+1 은 문자열에 존재하는 단어의 개수가 됨


print("-----------------------------------")
print("092 문자열에서 특정 문자(열) 위치 찾기(find)")
txt = 'A lot of Things occur each day, every day.'
offset1 = txt.find('e')
offset2 = txt.find('day')
offset3 = txt.find('day', 30)  # 찾기 시작할 시작점 지정
print(offset1)
print(offset2)
print(offset3)
'''
find() 는 문자열에서 특정문자나 문자열이 최초로 나타나는 위치에 대한 인덱스
찾을 수 없으면 -1 리턴
'''


print("-----------------------------------")
print("093 문자열을 특정 문자(열)로 분리하기(split)")
url = 'http://www.naver.com/news/today=20220121'
log = 'name:홍길동 age:19 sex:남자 nation:조선'

ret1 = url.split('/')
print(ret1)

ret2 = log.split()  # 인자가 없으면 디폴트로 공백을 구분자로 ..
for data in ret2:
    d1, d2 = data.split(':')
    print('%s -> %s'%(d1, d2))


print("-----------------------------------")
print("094 문자열을 특정 문자(열)로 결합하기(join)")
loglist = ['2022/01/21 10:12:13', '200', 'OK', '이 또한 지나가리라']
bond = ';'       # 연결할 문자를 세미콜론(;)
log = bond.join(loglist)   # join 의 인자는 리스트 !
print(log)
'''
join() 메소드는 split() 과는 반대
리스트 요소를 연결할 문자를 세미콜론(;)으로 할 것
'''


print("-----------------------------------")
print("095 문자열에서 특정 문자(열)를 다른 문자(열)로 바꾸기(replace)")
txt = 'My password is 1234'
ret1 = txt.replace('1', '0')
ret2 = txt.replace('1', 'python')
print(ret1)
print(ret2)

txt = '매일 많은 일들이 일어납니다.'
ret3 = txt.replace('매일', '항상')
ret4 = txt.replace('일', '사건')
print(ret3)
print(ret4)


print("-----------------------------------")
print("096 문자열을 바이트 객체로 바꾸기(encode)")
u_txt = 'I love python'
b_txt = u_txt.encode()
print(u_txt)
print(b_txt)   # b'I love python'
               # -> 실제 값은  73 32 108 111 118 101 32 112 121 116 104 111 110

ret1 = 'I' == u_txt[0]
ret2 = 'I' == b_txt[0]
print(ret1)  # True
print(ret2)  # False
'''
바이트 객체는 2진 스트림 데이터로써 컴퓨터의 메모리에 기록되는 값으로 이해하면 됨
예를 들어, 'I' 에 해당하는 코드값은 73
파이썬3 에서는 모든 문자열은 유니코드 문자열로 취급

encode() 메소드는 유니코드로 되어 있는 문자열을 인자로 지정된 인코딩 방식으로 
인코딩하여 바이트 객체로 반환(인자가 없으면 디폴트 UTF-8)

'''


print("-----------------------------------")
print("097 바이트 객체를 문자열로 바꾸기(decode)")
b_txt = b'A lot of things occur each day'
u_txt = b_txt.decode()
print(u_txt)
'''
파일을 바이너리 모드로 읽거나 네트워크를 통해 읽어들인 데이터는
대부분 2진 데이터 스트림인 바이트 객체
이 데이터를 파이썬3 에서 문자열로 활용하려면 decode() 이용
'''


print("-----------------------------------")
print("098 문자열을 정렬하기(sorted, join)")
#strdata = input('정렬할 문자를 입력하세요')
strdata = 'a가b나c다'
ret1 = sorted(strdata)   # 파이썬 내장함수
ret2 = sorted(strdata, reverse=True)
print(ret1)
print(ret2)
ret1 = ''.join(ret1)
ret2 = ''.join(ret2)
print('오를차순으로 정렬된 문자열은 <' + ret1 + '> 입니다.')
print('내림차순으로 정렬된 문자열은 <' + ret2 + '> 입니다.')
