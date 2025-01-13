'''
016 정수형 자료 이해하기
017 실수형 자료 이해하기
018 복소수형 자료 이해하기
019 대입 연산자 이해하기(=)
020 사칙 연산자 이해하기( , -, *, /, **)
'''

##################################################
print("016 정수형 자료 이해하기")
int_data = 10
bin_data = 0b10
oct_data = 0o10
hex_data = 0x10
long_data = 1234567890123456789

print(int_data)
print(bin_data)
print(oct_data)
print(hex_data)
print(long_data)
# 출력값은 10진수로 나옴


##################################################
print("017 실수형 자료 이해하기")
f1 = 1.0
f2 = 3.14
f3 = 1.56e3
f4 = -0.7e-4

print(f1)
print(f2)
print(f3)  # 1560.0
print(f4)  # -7e-05


##################################################
print("018 복소수형 자료 이해하기")
c1 = 1+7j
print(c1.real); print(c1.imag)
c2 = complex(2,3)
print(c2)
'''
복소수형 상수는 실수부+허수부 로 되어 있는 수 입니다.
  실수부만 취하려면 real 을 이용
  허수부만 취하려면 imag 를 이용
complex 를 이용해 복소수형 상수를 구성할 수 있음
  complex(2,3) -> 실수부 2, 허수부 3
  print 시  -> (2+3j) 출력
'''


##################################################
print("020 사칙 연산자 이해하기( , -, *, /, **)")

a = 2
b = 4
ret1 = a + b
ret2 = a - b
ret3 = a * b
ret4 = a / b
ret5 = a ** b
ret6 = a+a*b/a
ret7 = (a+b) * (a-b)
ret8 = a*b**a

print(ret1)
print(ret2)
print(ret3)
print(ret4)  # 0.5
print(ret5)
print(ret6)  # 6.0 (곱셈,나눗셈 먼저 계산)
print(ret7)
print(ret8)

