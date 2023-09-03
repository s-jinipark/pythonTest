
##### 이분검색
def solution():
    answer = 0
    '''
    고새 또 기억이 안남
    풀이보고 기억 살림
    '''
    # 소팅 먼저
    inp.sort()
    print(inp)

    # mid 계산
    lt = 0
    rt = N-1

    while lt <= rt:   # 같을 수 있음
        mid = (lt + rt) // 2
        if inp[mid] == M :
            print(mid +1)  # 몇 번째 를 출력하는 것이므로 +1
            answer = mid +1
            break
        elif inp[mid] > M :
            rt = mid -1
        else :
            lt = mid +1

    return answer
'''
mid 를 (rt-lt)//2 로 했는데...
(rt+lt)//2 임   (-> 주의)
'''
N = 8
M = 32
inp = [23,87,65,12,57,32,99,81]
re = solution()
print(re)
#=> 3


