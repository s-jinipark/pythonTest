
'''

파이썬에서 맵은 dictionary 라는 파이썬 내장 자료구조를 이용하면 됨
변수명 = {}

첫째줄에 테스트 케이스
  각 테스트 케이스의 첫재 쭐 -> 의상 수
  다음 n 개 -> 의상 이름 과 의상 종류
'''

import sys

sys.stdin = open("input10-4.txt", "rt")
case = int(input())  # n

for i in range(case) :
    num = int(input())
    item = {}  # [map 사용 위한]
    answer = 1  # **
    for j in range(num) :
        #print(input())
        i, c = input().split()
        if not c in item :
            item[c] = 1
        else :
            item[c] += 1
    print(item)

    for k in item.keys() :
        answer = answer * (item[k] +1)  # ?? +1 만 하면 됨? [선택 안함 포함]
    print(answer -1)

'''
{'headgear': 2, 'eyewear': 1} 라면
  . headgear 만 입는 경우  [ -> 선택안함 까지 3가지 경우]
  . eyewear 만 입는 경우
  . headgear, eyewear 를 동시에 입는 경우
  
  3C1 = 3 과 2C1 = 2 를 곱해준 후 전부를 입지 않은 경우 빼줌(-1)
  
'''