
##### 랜선자르기(결정알고리즘)

def Count(x):
    cnt = 0
    for i in inp:
        #print(i)
        cnt += i//x
    return cnt

def solution():
    answer = 0
    '''
    일단 rt 는 가장 큰 값 : 802
    mid 값을 구해 그 값으로 나누어 봄
    각 나누기 몫을 다 더해 -> 원하는 갯수를 만족하는지 .. 확인함 
    '''
    lt = 0
    rt = max(inp)

    min_val = 2147000000
    while (lt <= rt):
        mid = (lt + rt)//2
        # mid 로 개수를 계산해 봄
        print(Count(mid), mid)
        min_val = min(mid, min_val)
        if Count(mid) >= N: # 갯수를 넘는 것도 OK
            # 길이를 늘이면 갯수가 줄어드나?
            # mid 값을 올리는 것이니 .. lt 를 당김
            lt = mid +1
        else :
            rt = mid -1  # 이건 반대
    answer = min_val
    return answer


K = 4
N = 11

inp = [802,743,457,539]
re = solution()
print(re)
#=> 200


