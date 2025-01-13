
# 모의고사

# 문제 설명
# 수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 
# 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

# 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 
# 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

def solution(answers):
    answer = []
    std1 = [1, 2, 3, 4, 5]  # 5개 반복
    std2 = [2, 1, 2, 3, 2, 4, 2, 5]  # 8개 반복
    std3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  #10개 반복

    std_p = [0, 0, 0]  # 학생 점수

    # 계속 증가하는 수에 대응하여 배열이 반복되도록...
    for i in range( 0, 10 ):  # 0 부터 9까지 반복
        print(i, i%5)
        # 이렇게 반복이 됨
        # 0 0
        # 1 1
        # 2 2
        # 3 3
        # 4 4
        # 5 0  <- *
        # 6 1

    for i in range(0, len(answers) ):
        #print(std1[i%len(std1)])
        if answers[i] == std1[i%len(std1)]:
            std_p[0] += 1
        if answers[i] == std2[i%len(std2)]:
            std_p[1] += 1          
        if answers[i] == std3[i%len(std3)]:
            std_p[2] += 1  
    # 3명 이라 했음
    top_score = 0
    for j in std_p:
        if top_score < j:
            top_score = j

    # 한번 더 돌림
    for k in range(0, len(std_p)):
        if std_p[k] == top_score:
            answer.append(k+1)
    # sort 해줌
    answer.sort()

    return answer



a1 = [1,2,3,4,5]
an1 = solution(a1)
print(an1)

a1 = [1,3,2,4,2]
an1 = solution(a1)
print(an1)

