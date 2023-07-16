
##### 사과나무(BFS)

def solution():
    answer = 0

    '''
    BFS 는 생각이 잘 안나서.
    
    도형 + for loop 로 해 봄
    '''
    tmp = []
    mid = N//2+1  # 항상 홀수라니.. 반으로 나누고 +1
    print(mid)
    for i in range(N) :
        for j in range(N):
            if mid -i <= i <= mid+i:
                print(j, i)

N = 5

inp = [
    [10,13,10,12,15],
    [12,39,30,23,11],
    [11,25,50,53,15],
    [19,27,29,37,27],
    [19,13,30,13,19]
]

re = solution()
print(re)
#=>
print('====================')
