
##### 대표값
def solution():
    answer = 0

    print(sum(inp)/N, int(sum(inp)/N), round(sum(inp)/N))
    avg = round(sum(inp)/N)

    # 평균과 가장 가까운 점수가 여러 개일 경우 먼저 점수가 높은 학생의 번호를 답으로 하고,
    # 높은 점수를 가진 학생이 여러 명일 경우 그 중 학생번호가 빠른 학생의 번호를 답으로 합니다.
    ## 대응하기 위해서 dict 로
    tmp= dict()
    dp_val = 2147000000  # 대표값
    score = 0
    no = 2147000000

    for i in range(N):
        if abs(avg - inp[i]) <= dp_val :  # 작거나 같을 경우
            #print(abs(avg - inp[i]), dp_val, '->', inp[i])
            dp_val = abs(avg - inp[i])
            if score < inp[i] :
                score = inp[i]
                no = i
            elif score == inp[i] :
                if no > i :
                    no = i
    print(no + 1)
    return answer

N = 10
inp = [45, 73, 66, 87, 92, 67, 75, 79, 75, 80]
re = solution()
print(re)
#=> 74  7

N = 15
inp = [12, 34, 17, 6, 11, 15, 27, 42, 39, 31, 25, 36, 35, 25, 17]
re = solution()
print(re)
#=> 25  11  (난 25 2 가 나옴??)
