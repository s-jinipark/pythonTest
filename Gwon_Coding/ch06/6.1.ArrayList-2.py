
# 6-1-1 ArrayList 를 사용하는 예제
# N 개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성
n = 5
inp = "20 10 35 30 7"

lst1 = inp.split()
print(lst1)  #-> 문자열로 들어 감
lst2 = map(int, inp.split())
print(lst2)  #-> <map object at 0x000002BED5027670>  (이런 식으로 나옴)
lst3 = list(map(int, inp.split()) )
print(lst3)

print(min(lst3))
print(max(lst3))
#-> 함수 사용하면 이렇게 간편

