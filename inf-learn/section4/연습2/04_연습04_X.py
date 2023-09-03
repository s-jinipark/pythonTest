
##### 마구간 정하기(결정알고리즘)

def Count(x):   # 이번 문제는 여기를 잘 모르겠음
    cnt = 1
    # tot =0
    # for  i in inp:
    #     if i+tot >=n:
    #         cnt += 1
    #         tot = i
    #     else:
    #         tot += i

    # [2] 여기는 해설 보고 . . .  기존과 엇 비슷한데 응용 안됨
    ep = inp[0]   # end point
    for i in range(1, N):
        if inp[i]-ep >= x :
            cnt += 1
            ep = inp[i]
    return cnt

def solution():
    answer = 0
    inp.sort()
    lt = 1
    rt = max(inp)
    while lt <= rt:
        mid = (lt+rt)//2
        print(mid, Count(mid))
        if Count(mid) >= C :  # 답이 될 수 잇다는 얘기
            # 갯수를 줄이기 위해선 mid 가 커져야 겠지
            answer = mid
            lt = mid +1
        else :  # [2] 이건 너무 긴 경우
            rt = mid -1

    return answer

'''
생각해 봄
우선 sort 를 하고
이건 rt 를 max 로 하면 될 듯
mid 를 구한 뒤
C 개 를 배치할 수 있는지...

'''

N = 5
C = 3

inp = [1, 2, 8, 4, 9]
re = solution()
print('re', re)
#=>

