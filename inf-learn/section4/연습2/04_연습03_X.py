
##### 뮤직비디오(결정알고리즘)
def Count(n):
    #cnt = 0
    cnt = 1   # [2] 웁스 ! 여기 1부터 시작해야
    tmp = 0
    for i in inp:
        tmp += i
        if tmp > n:
            cnt +=1
            tmp = i
    return cnt

def solution():
    answer = 0
    lt = 1
    rt = sum(inp)
    print(lt, rt)
    while lt <= rt:
        mid = (lt+rt)//2
        print(mid, Count(mid))
        if Count(mid) <= M :
            answer = mid  # 갯수가 적게 나왔다. 그럼 mid 를 줄여야 겠네
            rt = mid -1   # 더 좋은 값을 찾기 위해 . . .
        else :
            lt = mid +1

    return answer

'''
풀이 설명 듣고 품
모든 곡을 다 더해서 그걸 max 로 삼는다.

'''

N = 9
M = 3

inp = [1, 2, 3, 4, 5, 6, 7, 8, 9]
re = solution()
print(re)
#=> 17 (난 15)

