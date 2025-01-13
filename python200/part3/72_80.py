'''
072 최대값, 최소값 구하기(max, min)
073 1바이트에서 하위 4비트 추출하기
074 1바이트에서 상위 4비트 추출하기
075 문자열에서 특정 위치의 문자 얻기
076 문자열에서 지정한 구간의 문자열 얻기
077 문자열에서 홀수 번째 문자만 추출하기
078 문자열을 거꾸로 만들기
079 두 개의 문자열 합치기( )
080 문자열을 반복해서 새로운 문자열로 만들기(*)
'''

print("-----------------------------------")
print("072 최대값, 최소값 구하기(max, min)")
listdata = [9.96, 1.27, 5.07, 6.45, 8.38, 9.29, 4.93, 7.73, 3.71, 0.93]
maxval = max(listdata)
minval = min(listdata)
print(maxval)  # 9.96
print(minval)  # 0.93

txt = 'Alotofthingsoccureachday'
maxval = max(txt)
minval = min(txt)
print(maxval)  # 'y'  (최대값은 알파벳 순서로 가장 뒤)
print(minval)  # 'A'

maxval = max(2+3, 2*3, 2**3, 3**2)
minval = min('abz', 'a12')
print(maxval)  # 9
print(minval)  # a12


print("-----------------------------------")
print("073 1바이트에서 하위 4비트 추출하기")
a = 107
b = a & 0x0f
print(b)

'''
숫자 107을 1바이트 단위 2진수로 표현하면 01101011 

        상위 4비트  |  하위 4 비트
2진수   0  1  1  0    1  0  1  1
16진수  6             B

16진수 0x6b 의 하위 4비트값만 추출하려면
이 값을 0x0f 와 비트단위 AND 연산 수행
즉
        상위 4비트  |  하위 4 비트
0x6b    0  1  1  0    1  0  1  1
0x0f    0  0  0  0    1  1  1  1
&연산 -> 0  0  0  0    1  0  1  1
결과  =>  0            b 
'''


print("-----------------------------------")
print("074 1바이트에서 상위 4비트 추출하기")
a = 107
b = (a>>4) & 0x0f
print(b)


print("-----------------------------------")
print("075 문자열에서 특정 위치의 문자 얻기")
txt1 = 'A tale that was not right'
txt2 = '이 또한 지나가리라.'
print(txt1[5])   # 'e' 출력
print(txt2[-2])  # '라' 출력


print("-----------------------------------")
print("076 문자열에서 지정한 구간의 문자열 얻기")
print(txt1[3:7])   # 'ale' 출력
print(txt1[:6])    # 'A tale' 출력
print(txt2[-4:])   # '가리라.'

'''
  'A tale that was not right'
   01234567
   '이    또  한    지  나  가  리  라  .'
    0  1  2   3  4  5  6   7   8   9  10
                      -5  -4  -3  -2 -1
'''


print("-----------------------------------")
print("077 문자열에서 홀수 번째 문자만 추출하기")
txt = 'aAbBcCdDeEfFgGhHiIjJkK'
ret = txt[::2]
print(ret)
# 짝수번째만 출력한다면
ret = txt[1::2]
print(ret)


print("-----------------------------------")
print("078 문자열을 거꾸로 만들기")
txt = 'abcdefghijk'
ret = txt[::-1]
print(ret)
# 주어진 문자열에서 거꾸로 된 순서로 홀수번째 문자만 추출
ret = txt[::-2]
print(ret)
# 주어진 문자열의 거꾸로 된 순서로 짝수번째 문자만 추출
ret = txt[-2::-2]
print(ret)


print("-----------------------------------")
print("079 두 개의 문자열 합치기(+)")
#filename = input("저장할 파일이름을 입력하시오")
#filename = filename + '.jpg'
#display_msg = '당신이 저장한 파일은 <' + filename + '> 입니다.'
#print(display_msg)

print("-----------------------------------")
print("080 문자열을 반복해서 새로운 문자열로 만들기(*)")
msg1 = '여러분'
msg2 = '파이팅!'
display_msg = msg1 + ', ' + msg2*3 + '~ !'
print(display_msg)
