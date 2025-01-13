'''
099 순차적인 정수 리스트 만들기(range)
100 리스트에서 특정 위치의 요소 얻기
101 리스트에서 특정 요소의 위치 구하기(index)
102 리스트에서 특정 위치의 요소를 변경하기
103 리스트에서 특정 구간에 있는 요소 추출하기
104 리스트에서 짝수 번째 요소만 추출하기
105 리스트 요소 순서를 역순으로 만들기 ① (reverse)
106 리스트 요소 순서를 역순으로 만들기 ② (reversed)
107 리스트 합치기(+)
108 리스트 반복하기(*)
109 리스트에 요소 추가하기(append)
110 리스트의 특정 위치에 요소 삽입하기(insert)
111 리스트의 특정 위치의 요소 제거하기(del)
112 리스트에서 특정 요소 제거하기(remove)
113 리스트에서 특정 구간에 있는 모든 요소 제거하기
114 리스트에 있는 요소 개수 구하기(len)
115 리스트에서 특정 요소 개수 구하기(count)
116 리스트 제거하기(del)
'''

print("-----------------------------------")
print("099 순차적인 정수 리스트 만들기(range)")
range1 = range(10)
range2 = range(10,20)
print(range1)  # range(0, 10)  (<- 이게 출력됨 , range 객체는 리스트가 아님에 유의)
print(list(range1))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  <- 9 까지
print(list(range2))

''' 
for 문의 일부인 줄 알았음
  ret = 0
  for i in range(10)
    ret += (i +1) 
'''


print("-----------------------------------")
print("100 리스트에서 특정 위치의 요소 얻기")
listdata = [1,2, 'a','b','c', [4,5,6]]
val1 = listdata[1]
val2 = listdata[3]
val3 = listdata[5][1]
print(val1)
print(val2)
print(val3)


print("-----------------------------------")
print("101 리스트에서 특정 요소의 위치 구하기(index)")
solarsys = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성','지구']
planet = '지구'
pos = solarsys.index(planet)
print('%s 는 태양계에서 %d 번째 위치하고 있습니다.'%(planet, pos))
pos = solarsys.index(planet, 5)
print('%s 는 태양계에서 %d 번째 위치하고 있습니다.'%(planet, pos))
# 지구 는 태양계에서 9 번째 위치하고 있습니다.  (인덱스 5 이상인 요소부터 검사, 0부터 계산하므로 9 가 나옴)


print("-----------------------------------")
print("102 리스트에서 특정 위치의 요소를 변경하기")
solarsys = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성']
planet = '화성'
pos = solarsys.index(planet)
solarsys[pos] = 'Mars'
print(solarsys)


print("-----------------------------------")
print("103 리스트에서 특정 구간에 있는 요소 추출하기")
solarsys = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성']
rock_planet = solarsys[1:4]
gas_planet = solarsys[4:]
print('태양계의 암석형 행성 : ', end='');print(rock_planet)
print('태양계의 가스형 행성 : ', end='');print(gas_planet)


print("-----------------------------------")
print("104 리스트에서 짝수 번째 요소만 추출하기")
listdata = list(range(1,21))
evenlist = listdata[::2]  # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19] 나옴
print(evenlist)
evenlist = listdata[1::2]  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20] 나옴
print(evenlist)


print("-----------------------------------")
print("105 리스트 요소 순서를 역순으로 만들기 ① (reverse)")
listdata = list(range(5))
listdata.reverse()
print(listdata)


print("-----------------------------------")
print("106 리스트 요소 순서를 역순으로 만들기 ② (reversed)")
listdata = list(range(5))
ret1 = reversed(listdata)
print(ret1)  # <list_reverseiterator object at 0x000002732AA9E108>
print('원본 리스트 ', end='');print(listdata)
print('역순 리스트 ', end='');print(list(ret1))

ret2 = listdata[::-1]
print('슬라이싱 이용 ', end='');print(ret2)


print("-----------------------------------")
print("107 리스트 합치기(+)")
listdata1 = ['a', 'b', 'c', 'd', 'e']
listdata2 = ['f', 'g', 'h', 'i', 'j']
listdata3 = listdata1 + listdata2
listdata4 = listdata2 + listdata1
print(listdata3)
print(listdata4)


print("-----------------------------------")
print("108 리스트 반복하기(*)")
listdata = list(range(3))
ret = listdata * 3
print(ret)


print("-----------------------------------")
print("109 리스트에 요소 추가하기(append)")
# listdata = []
# for i in range(3):
#     txt = input('리스트에 추가할 값을 입력하세요 [%d/3]: '%(i+1))
#     listdata.append(txt)
#     print(listdata)


print("-----------------------------------")
print("110 리스트의 특정 위치에 요소 삽입하기(insert)")
solarsys = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성']
pos = solarsys.index('목성')
solarsys.insert(pos, '소행성')  # 목성 위치에 들어가고 그 뒤는 하나씩 밀림.
print(solarsys)


print("-----------------------------------")
print("111 리스트의 특정 위치의 요소 제거하기(del)")
solarsys = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성']
del solarsys[0]
print(solarsys)
del solarsys[-2]
print(solarsys)


print("-----------------------------------")
print("112 리스트에서 특정 요소 제거하기(remove)")
solarsys = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성']
solarsys.remove('태양')
print(solarsys)


print("-----------------------------------")
print("113 리스트에서 특정 구간에 있는 모든 요소 제거하기")
solarsys = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성']
del solarsys[1:3]
print(solarsys)


print("-----------------------------------")
print("114 리스트에 있는 요소 개수 구하기(len)")
listdata = [2,2,1,3,8,5,7,6,3,6,2,3,9,4,4]
listsize = len(listdata)
print(listsize)


print("-----------------------------------")
print("115 리스트에서 특정 요소 개수 구하기(count)")
listdata = [2,2,1,3,8,5,7,6,3,6,2,3,9,4,4]
c1 = listdata.count(2)
c2 = listdata.count(7)
print(c1)
print(c2)


print("-----------------------------------")
print("116 리스트 제거하기(del)")
listdata = [2,2,1,3,8,5,7,6,3,6,2,3,9,4,4]
del listdata
#print(listdata)
# -> NameError: name 'listdata' is not defined