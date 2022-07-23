def func_a(n, ary):
    answer = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for i in range(len(ary)):  # 2차원 배열인데. ?
        #answer[@@@] = @@@
        answer[ ary[i][0] ][ ary[i][1] ] = ary[i][2]

    return answer

def func_b(idx, current, visited, ary):
    if visited[idx] == True or ary[current][idx] == 0:
        return True

    return False

def func_c(visited, ary, n, current, cnt, time):
    ret = 0xf111111

    if cnt > n and current ==1:
        return time

    for i in range(n+1):
        if func_b(i, current, visited, ary):
            continue

        visited[i] = True
        time += ary[current][i]
        #ret = min(ret, func_@@@(@@@))
        #ret = min(ret, func_c(visited, ary, n, current, cnt, time))  # 배껴서 했는데 아님
        ret = min(ret, func_c(visited, ary, n, i, cnt+1, time))
        time -= ary[current][i]
        visited[i] = False

    return ret

def solution(works, schedule):
    answer = 0
    visited = [False for i in range(works+1)]
    matrix = func_a(works, schedule)
    print(matrix)
    answer = func_c(visited, matrix, works, 1, 1, 0)

    return answer


works1 = 3
schedules1 = [[1,2,20],[2,3,25],[2,1,25],[1,3,20],[3,2,15],[3,1,20]]
res1 = solution(works1, schedules1)
print(res1)

works2 = 4
schedules2 = [[1,2,35],[2,3,10],[2,1,12],[1,3,16],[3,2,20],[3,1,10],[1,4,15],[4,3,30], [4,2,25],[2,4,20]]
res2 = solution(works2, schedules2)
print(res2)