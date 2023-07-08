
##### 이분검색
def solution():
    answer = 0
    inp.sort()
    print(inp)
    # 사실 여기서 끝난 건데. 이분검색으로
    # 이 형태가 패턴임
    lt = 0
    rt = N-1
    while (lt <= rt):
        mid = (lt+rt)//2
        if inp[mid] == M :
            print('>', mid, inp[mid], mid+1,'번째')
            break
        elif inp[mid] > M :
            rt = mid -1
        else :
            lt = mid +1

    return answer

N = 8
M = 32
inp = [23,87,65,12,57,32,99,81]
re = solution()
print(re)
#=> 3


