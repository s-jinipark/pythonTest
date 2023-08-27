
##### 안전영역(BFS)

from collections import deque


def solution():
    answer = 0

    '''
    기존 "섬나라 아일랜드" 와 유사
    
    물에 잠기는 부분을 먼저 처리 (ex : 0 으로)
    다음은 아일랜드와 거의 유사하게 .. 
    '''

    return answer

N = 5

inp = [
    [6, 8, 2, 6, 2],
    [3, 2, 3, 4, 6],
    [6, 7, 3, 3, 2],
    [7, 2, 5, 3, 6],
    [8, 9, 5, 2, 7]
]
#방문기록
ch = [[0]*N for _ in range(N)]

dx = [ -1, 0, 1, 0]  # 시계 방향으로
dy = [0, 1, 0, -1]

cnt = 0

re = solution()
print(re)
#=>
print('====================')
