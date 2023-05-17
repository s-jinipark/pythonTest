
# 프로그래머스 스타일 로 ...
def solution(N, M):
    answer = 0
    dict = {}
    for i in range(1, N+1):
        for j in range(1, M+1):
            print(i, j)
            tmp = i+j
            if tmp in dict :
                dict[tmp] += 1
            else :
                dict[tmp] = 1
    print(dict, max(dict.values()))
    maxVal = max(dict.values())
    tmp = []
    for i, k in enumerate(dict):
        print(i, k, dict[k])
        if maxVal == dict[k] :
            tmp.append(k)
    tmp.sort()
    answer = tmp
    return answer


N=4
M=6
re = solution(N, M)
print(re)
#=>

'''
두 개의 정 N면체와 정 M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중 
가장 확률이 높은 숫자를 출력하는 프로그램을 작성하세요.
'''
