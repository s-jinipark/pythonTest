def solution(land):
    answer = 0

    # 4 열 고정 , 밟았던 땅은 다음번에 skip => 최대값은 ?

    prev = -1
    for i in range(len(land)):

        max = 0
        for j in range(4):

            if j == prev :
                continue
            tmp = -1
            if max < land[i][j] :
                max = land[i][j]
                tmp = j
                print(i, j, prev)

        print(max)
        prev = tmp    # 적절한 위치 찾기 ...
        answer += max

    return answer


land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
re = solution(land)
print(re)

'''
통과 못함

'''