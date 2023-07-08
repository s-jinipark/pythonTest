
##### 대표값
def solution():
    answer = 0

    print(sum(inp)/N, int(sum(inp)/N), round(sum(inp)/N))
    avg = round(sum(inp)/N)

    # 평균과 가장 가까운 점수가 여러 개일 경우 먼저 점수가 높은 학생의 번호를 답으로 하고,
    # 높은 점수를 가진 학생이 여러 명일 경우 그 중 학생번호가 빠른 학생의 번호를 답으로 합니다.

    min_no = 2147000000
    res = 0
    score = 0
    for idx, x in enumerate(inp):
        #print(idx, x)
        tmp = abs(avg -x)
        #print(연습)
        if tmp < min_no :
            min_no = tmp
            res = idx+1   # 순번
            score = x
        elif tmp == min_no:  # 가까운 점수가 여러 개일 경우
            if x > score :   # 점수가 높은 학생의 번호...
                score = x
                res = idx + 1
            # 높은 점수를 가진 학생이 여러 명일 경우 그 중 학생번호가 빠른 학생의 번호를 답으로
            # [근데 이건 앞에서 부터 차례로 했기 때문에]
    print(avg, res)
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
#=> 25  11

N = 10
inp = [12,34,17,6,11,15,27,42,39,31]
re = solution()
print(re)
#=> 23 7

N = 5
inp = [1,2,3,4,5]
re = solution()
print(re)
#=> 3 3
