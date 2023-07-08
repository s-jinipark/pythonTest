
##### 뮤직비디오(결정알고리즘)

def Count(x):
    cnt = 0
    t_sum = 0
    for i in inp:
        #print(i)
        if t_sum + i > x:
            t_sum = i
            cnt += 1
        else :
            t_sum += i
    return cnt

def solution():
    answer = 0

    lt = 0
    rt = sum(inp)
    res = 0
    min_val = 2147000000
    while lt <= rt :
        mid = (lt+rt)//2
        print('>', Count(mid))
        if Count(mid) <= M :
            res = mid
            rt = mid -1   # 용량을 줄이는 거지.
            print('res', res)
            min_val = min(res, min_val)
        else :
            lt = mid +1
    answer = min_val
    
    return answer

'''
풀이 설명 듣고 품

근데, 답 틀림
'''

N = 9
M = 3

inp = [1, 2, 3, 4, 5, 6, 7, 8, 9]
re = solution()
print(re)
#=> 17 (난 15)

