# 다음과 같이 import를 사용할 수 있습니다.
# import math
from collections import deque

def solution(garden):
    # 여기에 코드를 작성해주세요.
    answer = 0

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    l_g = len(garden)
    qu = deque()
    chk = [[0] * l_g for _ in range(l_g)]
    print(garden)
    print('l_g', l_g)
    # start
    for i in range(l_g):  # 문제에 정사각형이라고
        for j in range(l_g) :
            print(i,j)
            if garden[i][j] == 1 :
                #print('k')
                qu.append((i,j))
                chk[i][j] = 0
    # -> 여기 까지가 셋팅

    # => 처리 시작
    lastNum = 0
    while qu :
        cx, cy = qu.popleft()
        print('>', cx, cy)
        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]
            if 0 <= nx < l_g and 0 <= ny < l_g :
                if garden[nx][ny] != 0: continue
                qu.append((nx,ny))
                garden[nx][ny]  = 1
                chk[nx][ny] = chk[cx][cy] +1
                lastNum = chk[nx][ny]   # 마지막 숫자를 넣는다? 꽃이 여러개 일때 안될거 같은데.. 흠
                answer += 1

    print('lastNum', lastNum)
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
garden1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
ret1 = solution(garden1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

garden2 = [[1, 1], [1, 1]]
ret2 = solution(garden2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")


'''
문제 설명
정사각형 크기 격자 모양 정원에 칸마다 핀 꽃 또는 피지 않은 꽃을 심었습니다. 
이 정원의 꽃이 모두 피는 데 며칠이 걸리는지 알고 싶습니다. 
핀 꽃은 하루가 지나면 앞, 뒤, 양옆 네 방향에 있는 꽃을 피웁니다.

현재 정원의 상태를 담은 2차원 리스트 garden이 주어졌을 때, 
모든 꽃이 피는데 며칠이 걸리는지 return 하도록 solution 함수를 작성해주세요.


매개변수 설명
현재 정원 상태를 담은 2차원 리스트 garden이 solution 함수의 매개변수로 주어집니다.

ㆍ 정원의 한 변의 길이는 2 이상 100 이하입니다.
ㆍ 정원 상태를 담은 2차원 리스트 garden의 원소는 0 또는 1 입니다.
ㆍ 이미 핀 꽃은 1로 아직 피지 않은 꽃은 0으로 표현합니다.
ㆍ 정원에 최소 꽃 한 개는 피어 있습니다.

return 값 설명
꽃이 모두 피는데 며칠이 걸리는지 return 합니다.

예제
garden	                            return
[[0, 0, 0], [0, 1, 0], [0, 0, 0]]	2
[[1, 1], [1, 1]]	                0

'''