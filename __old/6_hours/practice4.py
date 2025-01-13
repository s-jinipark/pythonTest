
# 리스트 []

#지하철 칸별로 10명, 20명, 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30

subway = [10, 20, 30]
print(subway)


subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호 몇번째 칸에 타고 있는가?
print(subway.index("조세호"))

# 하하 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print(subway)

# 정형돈을 유재석 / 조세호 사이에
subway.insert(1, "정형돈")
print(subway)

# 지하철에 있는 사람을 한명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

# 순서 뒤집기 가능
num_list.reverse()
print(num_list)

# 모두 지우기
# num_list.clear()
# print(num_list)

# 다양한 자료형 함께 사용
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)


print("----------")
# 사전
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(100) )

#print(cabinet[5]) # KeyError: 5
print(cabinet.get(5)) # None 출력 후 "hi" 찍는다 -> 다른 점
print("hi")

print(cabinet.get(5, "사용 가능")) # 없을 경우 대체 값

print(3 in cabinet) # True
print(5 in cabinet) # False

print("----------")
cabinet2 = {"A-3":"유재석" , "B-100":"김태호"}
print(cabinet2["A-3"])
print(cabinet2["B-100"])

# 새 손님
print(cabinet2)
cabinet2["A-3"] = "김종국"
cabinet2["C-20"] = "조세호"
print(cabinet2)

# 간 손님
del cabinet2["A-3"]
print(cabinet2)

# key 들만 출력
print(cabinet2.keys())

# value 들만 출력
print(cabinet2.values())

# key , value 쌍으로 출력
print(cabinet2.items())

# 폐점
cabinet2.clear()
print(cabinet2)

print("----------")
# 튜플

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

#menu.add("생선까스") # -> AttributeError: 'tuple' object has no attribute 'add'

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby) 

print("----------")
# 집합 (Set)
# 중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (java 와 python 을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java 할 수 있거나 python 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (java 할 수 있지만 python 은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# python 할 줄 아는 사람 늘어남
python.add("김태호")
print(python)

# java 를 잊었어요
java.remove("김태호")
print(java)

print("----------")
# 자료 구조의 변경
# 커피숍
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))
