
def solution(n, k, rocks):
    answer = 0
    tmp = 0
    for i in range(len(rocks)):
        print(rocks[i], i%n +1)
        tmp += rocks[i]
        if tmp >= k :  # 이 경우 가져 갔다는 소리
            print(tmp)
            answer = i%n +1
            break
    return answer


n = 3   # 참가자 수
k = 10  # 승리 돌
rocks = [2,3,1,2,3,2]

an = solution(n, k, rocks)

print(an)