'''
117 리스트 요소 정렬하기 ① (sort)
118 리스트 요소 정렬하기 ② (sorted)
119 리스트 요소 무작위로 섞기(shuffle)
120 리스트의 모든 요소를 인덱스와 쌍으로 추출하기(enumerate)
121 리스트의 모든 요소의 합 구하기(sum)
122 리스트 요소가 모두 참인지 확인하기(all, any)
123 사전에 요소 추가하기
124 사전의 특정 요소값 변경하기
125 사전의 특정 요소 제거하기(del)
126 사전의 모든 요소 제거하기(clear)
127 사전에서 키만 추출하기(keys)
128 사전에서 값만 추출하기(values)
129 사전 요소를 모두 추출하기(items)20
130 사전에 특정 키가 존재하는지 확인하기(in)
131 사전 정렬하기(sorted)
132 문자 코드값 구하기(ord)
133 코드값에 대응하는 문자 얻기(chr)
134 문자열로 된 식을 실행하기(eval)
135 이름없는 한줄짜리 함수 만들기(lambda)
136 인자를 바꾸어 함수를 반복 호출하여 결과값 얻기(map)
'''

print("-----------------------------------")
print("117 리스트 요소 정렬하기 ① (sort)")
namelist = ['Mary', 'Sams', 'Aimy', 'Tom', 'Michale', 'Bob', 'Kelly']
namelist.sort()
print(namelist)
namelist.sort(reverse=True)
print(namelist)

print("-----------------------------------")
print("118 리스트 요소 정렬하기 ② (sorted)")
namelist = ['Mary', 'Sams', 'Aimy', 'Tom', 'Michale', 'Bob', 'Kelly']
ret1 = sorted(namelist)
ret2 = sorted(namelist, reverse=True)
print(namelist)
print(ret1)
print(ret2)


print("-----------------------------------")
print("119 리스트 요소 무작위로 섞기(shuffle)")
from random import shuffle

listdata = list(range(1,11))
for i in range(3):
    shuffle(listdata)
    print(listdata)   # 출력결과는 실행할 때마다 달라짐


print("-----------------------------------")
print("120 리스트의 모든 요소를 인덱스와 쌍으로 추출하기(enumerate)")
solarsys = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성']
ret = list(enumerate(solarsys))
print(ret)

for i, body in enumerate(solarsys):
    print('태양계의 %d 번째 천체 : %s'%(i, body))

'''
enumerate() 은 시퀀스 자료형을 인자로 받아 
각 요소를 인덱스와 함께 쌍으로 추출할 수 있는 반복 가능한 자료인 enumerate 객체로 리턴
'''


print("-----------------------------------")
print("121 리스트의 모든 요소의 합 구하기(sum)")
listdata = [2,2,1,3,8,5,7,6,3,6,2,3,9,4,4]
ret = sum(listdata)
print(ret)


print("-----------------------------------")
print("122 리스트 요소가 모두 참인지 확인하기(all, any)")
listdata1 = [0,1,2,3,4]
listdata2 = [True, True, True]
listdata3 = ['',[],(),{},None, False]
print(all(listdata1))   # False  ( 0 때문)
print(any(listdata1))   # True
print(all(listdata2))   # True
print(any(listdata2))   # True
print(all(listdata3))   # False  (빈문자열, 빈리스트[], 빈튜플(), 빈사전{}, None)
print(any(listdata3))   # False


print("-----------------------------------")
print("123 사전에 요소 추가하기")
solar1 = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성']
solar2 = ['Sun', 'Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
solardict = {}
for i , k in enumerate(solar1) :
    val = solar2[i]
    solardict[k] = val

print(solardict)
# 순서가 없는 사전 자료임.. 다를 수 있음


print("-----------------------------------")
print("124 사전의 특정 요소값 변경하기")
names = {'Mary':10999 , 'Sams':2111, 'Aimy':9778, 'Tom':20245,
         'Michale':27115, 'Bob':5997, 'Kelly':7855}
names['Aimy'] = 10000
print(names)


print("-----------------------------------")
print("125 사전의 특정 요소 제거하기(del)")
names = {'Mary':10999 , 'Sams':2111, 'Aimy':9778, 'Tom':20245,
         'Michale':27115, 'Bob':5997, 'Kelly':7855}
del names['Sams']
print(names)


print("-----------------------------------")
print("126 사전의 모든 요소 제거하기(clear)")
names = {'Mary':10999 , 'Sams':2111, 'Aimy':9778, 'Tom':20245,
         'Michale':27115, 'Bob':5997, 'Kelly':7855}
names.clear()
print(names)


print("-----------------------------------")
print("127 사전에서 키만 추출하기(keys)")
names = {'Mary':10999 , 'Sams':2111, 'Aimy':9778, 'Tom':20245,
         'Michale':27115, 'Bob':5997, 'Kelly':7855}
ks = names.keys()
print(ks)  # dict_keys(['Mary', 'Sams', 'Aimy', 'Tom', 'Michale', 'Bob', 'Kelly'])
           # dict_keys 사전 뷰 객체로 리턴
key_list = list(ks)
print(key_list)

for k in key_list:
    print('Key : %s \t Value : %d'%(k,names[k]))

print("-----------------------------------")
print("128 사전에서 값만 추출하기(values)")
names = {'Mary':10999 , 'Sams':2111, 'Aimy':9778, 'Tom':20245,
         'Michale':27115, 'Bob':5997, 'Kelly':7855}
vals = names.values()
print(vals)   # dict_values([10999, 2111, 9778, 20245, 27115, 5997, 7855])

vals_lsit = list(vals)
print(vals_lsit)
ret = sum(vals_lsit)
print('출생아 수 총계 : %d '%ret)


print("-----------------------------------")
print("129 사전 요소를 모두 추출하기(items)")
names = {'Mary':10999 , 'Sams':2111, 'Aimy':9778, 'Tom':20245,
         'Michale':27115, 'Bob':5997, 'Kelly':7855}
items = names.items()
print(items)
# dict_items([('Mary', 10999), ('Sams', 2111), ('Aimy', 9778), ('Tom', 20245), ('Michale', 27115), ('Bob', 5997), ('Kelly', 7855)])

for item in items:
    print(item)
'''
('Mary', 10999)
('Sams', 2111) ...

'''


print("-----------------------------------")
print("130 사전에 특정 키가 존재하는지 확인하기(in)")
names = {'Mary':10999 , 'Sams':2111, 'Aimy':9778, 'Tom':20245,
         'Michale':27115, 'Bob':5997, 'Kelly':7855}
#k = input('이름을 입력하세요 : ')
k = 'Mary'
if k in names:
    print('이름이 <%s> 인 출생아 수는 <%d> 명 입니다.'%(k, names[k]))
else:
    print('자료에  <%s> 인 이름이 존재하지 않습니다.'%k )

'''
특정 값을 확인하려면
if 2111 in names.values() :
  ...
'''


print("-----------------------------------")
print("131 사전 정렬하기(sorted)")
names = {'Mary':10999 , 'Sams':2111, 'Aimy':9778, 'Tom':20245,
         'Michale':27115, 'Bob':5997, 'Kelly':7855}
ret1 = sorted(names)
print(ret1)  # key 만 나옴

def f1(x):
    return x[0]

def f2(x):
    return x[1]

ret2 = sorted(names.items(), key=f1)
print(ret2)
ret3 = sorted(names.items(), key=f2)
print(ret3)
ret4 = sorted(names.items(), key=f2, reverse=True)
print(ret4)


print("-----------------------------------")
print("132 문자 코드값 구하기(ord)")
#ch = input('문자 1개 입력')
ch = 'a'
if len(ch) != 0 :
    ch = ch[0]
    chv = ord(ch)
    print('문자 : %s \t 코드값 : %d [%s] '%(ch, chv, hex(chv)))


print("-----------------------------------")
print("133 코드값에 대응하는 문자 얻기(chr)")
val = 97
val = int(val)
try :
    ch = chr(val)
    print('코드값 : %d , 문자 : %s'%(val, ch))
except :
    print('입력한 <%d> 에 대한 문자가 존재하지 않습니다.'%val )


print("-----------------------------------")
print("134 문자열로 된 식을 실행하기(eval)")
expr1 = '2+3'
expr2 = 'round(3.7)'
ret1 = eval(expr1)
ret2 = eval(expr2)
print('<%s> 를 eval() 로 실행 : '%expr1, end='');print(ret1)
print('<%s> 를 eval() 로 실행 : '%expr2, end='');print(ret2)


print("-----------------------------------")
print("135 이름없는 한줄짜리 함수 만들기(lambda)")
add = lambda x, y: x+y
ret = add(1,3)
print(ret)   # 4

funcs = [lambda x : x+'.pptx', lambda x : x+'.docx']
ret1 = funcs[0]('intro')
ret2 = funcs[1]('Report')
print(ret1)   # intro.pptx
print(ret2)   # Report.docx

names = {'Mary':10999 , 'Sams':2111, 'Aimy':9778, 'Tom':20245,
         'Michale':27115, 'Bob':5997, 'Kelly':7855}
ret3 = sorted(names.items(), key=lambda x:x[0])
print(ret3)

'''
파이썬에서 함수를 정의하는 방법
def 함수이름(인자, ...)
  실행코드

lambda 함수는 이름없이 한줄로
lambda 인자, 인자, ... : 실행코드

'''


print("-----------------------------------")
print("136 인자를 바꾸어 함수를 반복 호출하여 결과값 얻기(map)")
f = lambda x : x*x
args = [1,2,3,4,5]
ret = map(f, args)
print(list(ret))
# [1, 4, 9, 16, 25]

f = lambda x, y : x * x + y
X = [1,2,3,4,5]
Y = [10,9,8,7,6]
ret = map(f, X, Y)  # 두개 이상의 반복되는 인자에 대해서도 적용 가능
#print(ret)  # <map object at 0x000001ADE9445148>
print(list(ret))
