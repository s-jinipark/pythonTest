
##### 뮤직비디오(결정알고리즘)

def Count(x):
    # sum = inp[0]
    # count = 0
    # for i in range(1,  N):
    #     if sum + inp[i] > x :
    #         sum = inp[i]
    #         count += 1
    ##### 풀이 보고
    sum = 0
    count = 1
    for i in inp:
        if sum + i > x:
            count += 1
            sum = i
        else :
            sum += i
    return count

def solution():
    answer = 0

    # 이거 선정하는 것도.. 쉽지 않아.
    lt = 1
    rt = sum(inp) # 9  # 처음에 9로 선정함  => 노래를 다 합친 수 45
    print('rt:', rt)
    #min_val = 2147000000   # [1]
    #res = 2147000000   # 여기를 그냥 0 으로 해도 ...
    res = 0
    maxx = max(inp) # [2] 반례 관련
    while lt <= rt:
        mid = (lt+rt)//2
        print(Count(mid), mid)
        # CD 갯수가 많이 나왔어 .. 그럼 길이를 더 늘려야 겠지
        #if Count(mid) <= M :  # 적은 경우도 정답 후보
        # [2] 반례 관련
        if mid >= maxx and Count(mid) <= M:  # 적은 경우도 정답 후보
            #res = min(mid, res)  # [1]
            res = mid  # 자동 갱신
            rt = mid - 1
        else:
            lt = mid + 1
    answer = res
    return answer

N = 9
M = 3

inp = [1, 2, 3, 4, 5, 6, 7, 8, 9]
re = solution()
print(re)
#=> 17

# [2] 반례가 나왔음 => 1 이 나옴 , 최대 가 9 이기 때문에 9 는 나와야 됨...
N = 9
M = 9

inp = [1, 2, 3, 4, 5, 6, 7, 8, 9]
re = solution()
print(re)


