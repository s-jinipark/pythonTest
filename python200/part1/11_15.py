'''11-15'''

'''
011 for문 개념 배우기 ① (for)
'''
scope = [1,2,3,4,5]
for x in scope :
    print(x)
'''
for 변수 in 범위 :
   반복으로 실행할 코드
for 문의 범위로 사용되는 것은 시퀀스 자료형 또는 반복 가능한 자료여야 함
'''
# . 문자열
str = 'abcdef'
for c in str :
    print(c)

# . 리스트나 튜플
# . 사전
ascii_codes = {'a':97, 'b':98, 'c':99}
for c in ascii_codes :
    print(c)
    # key 가 나옴.

# . range()
for c in range(10):
    print(c)
    # 0 ~ 9 가 나옴.

# . 그 외 반복 가능한 객체


##################################################
print("012 for문 개념 배우기 ② (for~continue~break)")
scope = [1,2,3,4,5]
for x in scope:
    print(x)
    if x < 3 :
        continue
    else :
        break


##################################################
print("013 for문 개념 배우기 ③ (for~else)")
scope = [1,2,3]
for x in scope :
    print(x)
else :
    print("Perfect")

# for 반복문이 break 없이 모두 실행되어야만 특정 코드 실행
# [큰 의미는 없어 보임]


##################################################
print("014 while문 개념 배우기(while~continue~break)")
'''
for 문이 범위가 지정된 자료나 반복이 가능한 객체를 이용해 반복문을 수행하는 것이라면
while 문은 특정 조건을 만족하는 경우 지속적으로 반복을 수행하는  반복문

while 조건 :
  반복실행 코드
  continue  # while 구문 처음으로 이동하여 반복문 계속
  ...
  break     # while 구문을 탈출함
'''


##################################################
print("015 None 개념 배우기")
val = None
condition = 1
if condition == 1 :
    val = [1,2,3]
else :
    val = 'I love Python'

'''
None 은 Types.NoneType 의 유일한 값으로, 값이 존재하지 않는 변수에 대입하여
이 변수에 아무런 값이 없다는 것을 나타내기 위해 주로 활용된다
[null 과 유사한 듯]
'''
