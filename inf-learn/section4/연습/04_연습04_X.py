
##### 마구간 정하기(결정알고리즘)

def Count(x):
    # 여기 잘 모르겠음 [풀이 들으면서 푼다]
    ep = inp[0]  # 마지막 배치 지점
    cnt = 1
    for i in range(1, N):
        # 마지막 배치 지점하고, 새로 배치할 지점의 차이
        if inp[i]-ep >= x:
            cnt += 1
            ep = inp[i]
    return cnt

def solution():
    answer = 0

    lt = 1
    rt = max(inp)
    inp.sort()   # sort를 꼭 해야함

    while lt<= rt:
        mid = (lt+rt)//2   # mid 값이 가까운 말의 거리.
        print(Count(mid))
        if Count(mid) >= C:
            res = mid
            lt = mid +1
        else:
            rt = mid -1
    answer = res
    return answer

'''
풀이 설명 듣고 품

lt -> 1 , rt 는 ?? 9 를 넘지는 않음..
mid 가 가장 가까운 거리..
좌표를 for  loop 돌면서, mid 의 차이가 나야...
말을 넣을 수 있다...!!!

이러다 보면 3마리를 배치 못할 수도 있음
그렇다면.. 간격을 줄여야...

'''

N = 5
C = 3

inp = [1, 2, 8, 4, 9]
re = solution()
print('re', re)
#=>

