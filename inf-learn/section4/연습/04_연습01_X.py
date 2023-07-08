
##### 이분검색
def solution():
    answer = 0
    #mid = N//2
    lt = 0
    rt = N-1
    inp.sort()
    #print(lt, mid, rt)
    cnt =0

    while lt <= rt:
        mid = (lt+rt)//2
        if inp[mid] == M :
            print(mid+1)
            break
        elif inp[mid] > M:
            rt = mid-1
        else :
            lt = mid+1

    ##### first
    # while cnt < 6:
    #     if inp[mid] == M :
    #         print('>', inp[mid])
    #         break
    #     elif inp[mid] > M :
    #         rt = mid -1
    #         mid = (rt-lt)//2
    #     elif inp[mid] < M :
    #         lt = mid +1
    #         mid = (rt-lt)//2
    #     cnt += 1
    #     print(lt, mid, rt)

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


