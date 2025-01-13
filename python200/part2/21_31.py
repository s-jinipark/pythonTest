'''
021 연산자 축약 이해하기( =, -=, *=, /=)
022 True와 False 이해하기
023 관계 연산자 이해하기(==, !=, ＜, ＜=, ＞, ＞=)
024 논리 연산자 이해하기(and, or, not)
025 비트 연산자 이해하기(&, |, ~, ^, ＞＞, ＜＜)
026 시퀀스 자료형 이해하기
027 시퀀스 자료 인덱싱 이해하기
028 시퀀스 자료 슬라이싱 이해하기
029 시퀀스 자료 연결 이해하기(+)
030 시퀀스 자료 반복 이해하기(*)
031 시퀀스 자료 크기 이해하기(len)
'''

##################################################
print("021 연산자 축약 이해하기( =, -=, *=, /=)")
a = 0
a += 1
print(a)
a *= 4
print(a)
a /= 2
print(a)  # 주의) 2.0


##################################################
print("023 관계 연산자 이해하기(==, !=, ＜, ＜=, ＞, ＞=)")
x = 1 ; y =2
str1 = 'abc'; str2 = 'python'
print(x == y)
print(x != y)
print(str1 == str2)
print(str2 == 'python')
print(str1 < str2)  # True [문자열의 크기는 문자열의 사전 순서로 비교]


##################################################
print("024 논리 연산자 이해하기(and, or, not)")
bool1 = True; bool2 = False; bool3 = True; bool4 = False
print(bool1 and bool2)  # False
print(bool1 and bool3)  # True
print(bool2 or  bool3)  # True
print(bool2 or  bool4)  # False
print(not  bool1)  # False
print(not  bool2)  # True


##################################################
print("025 비트 연산자 이해하기(&, |, ~, ^, ＞＞, ＜＜)")
bit1 = 0x61  # 16진수 0x 로 시작     => 0110 0001
bit2 = 0x62                 #       => 0110 0010
print(hex(bit1 & bit2))     # 0x60  => 0110 0000
print(hex(bit1 | bit2))     # 0x63  => 0110 0011
print(hex(bit1 ^ bit2))     # 0x3   => 0000 0011  (두개의 비트값이 다를 경우 1, 같으면 0)
print(hex(bit1 >> 1))       # 0x30  => 0011 0000  (오른쪽 시프트 : 오른쪽 비트는 없어지고 왼쪽은 0으로 채워짐)
print(hex(bit1 << 2))       # 0x184 => 0001 1000 0100  (왼쪽 시프트)
                            # 1이 시작되기 전까지 왼쪽 비트는 없어지고 오른쪽 비트는 0으로 채워짐
                            # 즉, 이동하는 비트가 1 인 경우에는 그 값이 보존됨
'''
비트 연산자      의미
A & B           A와 B 의 비트간 and 연산을 수행함
A | B           A와 B 의 비트간 or 연산을 수행함
A ^ B           A와 B 의 비트간 배타적 논리합 xor 연산을 수행함
~ A             A의 비트를 반전시킴. 즉 A의 1의 보수를 만듬
A >> n          A의 모든 비트르 n 만큼 오른쪽으로 시프트 시킴
A << n          A의 모든 비트르 n 만큼 왼쪽으로 시프트 시킴

'a' => 0 1 1 0   0 0 0 1
       -------   -------
      상위 4비트   하위 4비트
          6          1
          
1 바이트를 2진수로 표현하면 8 자리 숫자가 되어 읽기에는 조금 김
편이상 두자리 16진수로 표현 => 'a' 는 '61' 로 표현됨
'''


##################################################
print("026 시퀀스 자료형 이해하기")
strdata = 'abcde'
listdata = [1,[2,3], '안녕']
tupledata = (100, 200, 300)
print(tupledata)
'''
특성            설명
인덱싱         인덱스를 통해 해당 값에 접근할 수 있음. 인덱스는 0 부터 시작.
슬라이싱        특정 구간의 값을 취할 수 있음.  구간은 시작 인덱스와 끝 인덱스로 정의. 
연결          '+' 연산자를 이용해 두 시퀀스 자료를 연결
반복          '*' 연산자를 이용해 시퀀스 자료를 여러번 반복
멤버체크        'in' 키워드를 사용하여 특정 값이 시퀀스 자료의 요소로 속해 있는지 확인
크기정보        len() 을 이용해 시퀀스 자료의 크기를 알 수 있음
'''


##################################################
print("027 시퀀스 자료 인덱싱 이해하기")
strdata = 'Time is money'
listdata = [1,2,[1,2,3]]

print(strdata[5])           # 'i' 가 출력됨
print(strdata[-2])          # 'e' 가 출력됨
print(listdata[0])          # 1 이 출력됨
print(listdata[-1])         # [1,2,3] 이 출력됨
print(listdata[2][-1])      # 3 이 출력됨
'''
strdata     T   i   m   e       i   s       m   o   n    e    y
인덱스       0   1   2   3   4   5   6   7   8   9   10   11   12
           -13 -12 -11 -10  -9  -8  -7  -6  -5  -4  -3   -2   -1 
'''


##################################################
print("028 시퀀스 자료 슬라이싱 이해하기")

strdata = 'Time is money!!'
print(strdata[1:5])
print(strdata[:7])  # Time is
print(strdata[9:])  # oney!!
print(strdata[:-3]) # Time is mone (? -3 위치는 빠짐)
print(strdata[-3:]) # y!! (? -3 위치도 출력)
print(strdata[:])
print(strdata[::2]) # Tm smny! (스텝 2)

'''
[:n]  처음부터 인덱스 n 미만인 요소까지 슬라이싱
[:-n]  처음부터 끝에서 n번째 미만인 요소까지 슬라이싱
'''


##################################################
print("029 시퀀스 자료 연결 이해하기(+)")
strdata1 = 'I love '; strdata2 = 'Python'; strdata3 = 'you'
listdata1 = [1,2,3]; listdata2 = [4,5,6]

print(strdata1 + strdata2)
print(strdata1 + strdata3)
print(listdata1 + listdata2)


##################################################
print("030 시퀀스 자료 반복 이해하기(*)")
artist = 'BTS!'
fan = 'ARMy'
dispdata = fan + ' 들이 외칩니다. ' + artist*3
print(dispdata)

'''
만약 [1,2,3]*3 을 수행하면
[1,2,3,1,2,3,1,2,3] 이 됨
'''


##################################################
print("031 시퀀스 자료 크기 이해하기(len)")
strdata1 = 'I love python'
strdata2 = '나는 파이썬을 사랑합니다'
listdata = ['a', 'b', 'c', strdata1, strdata2]

print(len(strdata1))  # 13 출력
print(len(strdata2))  # 13 출력
print(len(listdata))  # 5 출력
print(len(listdata[3])) # 13 출력
