'''01-10'''

'''
006 자료형 개념 배우기
1. 수치형 자료
  . 정수형 상수
  . 실수형 상수
  . 복소수형 상수
2. 문자열 자료

3. 리스트 자료
  리스트 자료는 '[]' 안에 임의의 객체를 순서 있게 나열한 자료형
  각 요소는 콤마(,) 로 구분
4. 튜플 자료
  튜플은 리스트와 비슷하지만 요소 값을 변경할 수 없다는 것이 리스트와 다름
5. 사전 자료
  사전 자료는 '{}' 안에 '키:값' 으로 된 쌍이 요소로 구성된 순서가 없는 자료형
  각 요소는 콤마로 구분하여 나열
'''


'''
007 자료형 출력 개념 배우기
'''
a = 200
msg = 'I love python'
list_data = ['a', 'b', 'c']
dict_data = {'a':97, 'b':88}

print(a)
print(msg)
print(list_data)
print(list_data[0])
print(dict_data)
print(dict_data['a'])

# print() 는 기본적으로 줄바꿈
# 한줄 출력을 위해선
print('#', end="")
print('#')


'''
009 if문 개념 배우기 ① (if~else)
'''
x = 1
y = 2
if x > y :
    print("x가 큼")
else :
    print("y가 크거나 같음")


'''
010 if문 개념 배우기 ② (if~elif)
'''
x = 1
y = 2
if x > y :
    print("x 가 y 보다 큽니다.")
elif x < y :
    print('x 가 y 보다 작습니다.')
else :
    print('x 와 y 가 같습니다.')

'''
011 for문 개념 배우기 ① (for)
012 for문 개념 배우기 ② (for~continue~break)
013 for문 개념 배우기 ③ (for~else)
014 while문 개념 배우기(while~continue~break)
'''
