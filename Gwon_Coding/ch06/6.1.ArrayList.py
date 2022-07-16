
# 6-1-1 ArrayList 를 사용하는 예제
# N 개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성
n = 5
inp = "20 10 35 30 7"

#array_list = list( inp.split())   # 이건 -> ['20', '10', '35', '30', '7']
array_list = list(map(int, inp.split()))

print(array_list)

max_num = array_list[0]
min_num = array_list[0]

for num in array_list:
    #print(num)
    if max_num < num :
        max_num = num
    if min_num > num :
        min_num = num
print(min_num, max_num)

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
score = 0
for i in range(5) :
    sum = 0
    for j in range(4) :
        sum += human[i][j]     # 원래 이렇게 하는데 , 위에는 잘 못 한 듯
        humanScore[i] = sum    # 합을 따로 저장
        score=max(score, sum)  # max 함수를 주로 쓰자

for i in range(5):
    if humanScore[i] == score :
        print(i+1, score)
        break

# 6-1-3 삽입과 삭제가 많은 ArrayList 의 잘못된 사용 예
# N 자리 숫자가 주어질 때, 여기서 숫자 K 개를 지워서 얻을 수 있는 가장 큰 수를 구하는 프로그램
# 예제 입력 4 2         출력
#          1924        94
# 예제 입력 7 3         출력
#          1231234     3234
# 예제 입력 10 4        출력
#          4177252841  775841

