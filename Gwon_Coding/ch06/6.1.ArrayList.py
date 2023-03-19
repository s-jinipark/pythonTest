
# 6-1-1 ArrayList 를 사용하는 예제
# N 개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성
n = 5
inp = "20 10 35 30 7"

#array_list = list( inp.split())   # 이건 -> ['20', '10', '35', '30', '7']
array_list = list(map(int, inp.split()))

print(array_list)

max_num = array_list[0]
min_num = array_list[0]  # 배열의 첫 번째 값으로 초기화

for num in array_list:
    #print(num)
    if max_num < num :
        max_num = num
    if min_num > num :
        min_num = num
print(min_num, max_num)

print("--------------------")
# 6-1-2 2차원 배열 사용 예제
# 각 참가자는 음식을 만들어 오고, 서로 다른 사람의 음식을 점수로 평가한다.
# 가장 많은 점수를 얻은 사람
# 예제 입력 5 4 4 5          출력
#          5 4 4 4          4 19 (우승자의 번호와 얻은 점수)
#          5 5 4 4
#          5 5 5 4
#          4 4 4 5

#human=[list(map(int, input().split())) for _ in range(5)]
human =  [[5, 4, 4, 5], [5, 4, 4, 4], [5, 5, 4, 4], [5, 5, 5, 4], [4, 4, 4, 5]]
print(human)
humanScore = [0] * 5   # [0 * 5] 이거 아님
print(humanScore)
max_sc = 0
max_sc_ord = 0
tmp_human_ord =0
for sc_list in human :
    tmp_sum = 0
    tmp_human_ord += 1
    for sc in sc_list:
        tmp_sum += sc
    if max_sc < tmp_sum :
        max_sc = tmp_sum
        max_sc_ord = tmp_human_ord
print(max_sc_ord, max_sc)
print("--------------------")
humanScore = [0] * 5    # 참가자들의 총합 점수를 저장하기 위한 배열 생성
score = 0               # 최대 점수를 저장하기 위한 변수 생성
for i in range(5) :
    sum = 0
    for j in range(4) :
        sum += human[i][j]     # 책에 이렇게  , 위에는 내가
    humanScore[i] = sum    # 합을 따로 저장
    score=max(score, sum)  # max 함수를 주로 쓰자

for i in range(5):
    if humanScore[i] == score :  # 참가자의 총 점수가 최대점수 라면
        print(i+1, score)
        break

print("--------------------")
# 6-1-3 삽입과 삭제가 많은 ArrayList 의 잘못된 사용 예
# N 자리 숫자가 주어질 때, 여기서 숫자 K 개를 지워서 얻을 수 있는 가장 큰 수를 구하는 프로그램
# 예제 입력 4 2         출력
#          1924        94
# 예제 입력 7 3         출력
#          1231234     3234
# 예제 입력 10 4        출력
#          4177252841  775841


# [책->]탐욕법 알고리즘과 스택 자료구조가 무엇인지 알아야 정확히 풀이를 할 수 있다
# 7장 스택에서 ...

# [내 나름 풀이] 숫자를 지우는 거니까 , 순서 보장
# 순열을 써야 될 듯

from itertools import permutations

n, k = 4, 2
inp = "1924"

lst = list(inp)
print(lst)
lst2 = list(permutations(lst,2))
print(lst2)
max_num = 0
for l in lst2 :
    #print(l[0] + l[1])
    tmp = int(l[0] + l[1])
    if tmp > max_num :
        max_num = tmp
print(max_num)

