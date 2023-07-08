
##### 스토쿠 검사
def solution():
    answer = 0
    t_sum = 0
    for i in range(1, 10):
        t_sum += i
    print(t_sum)

    # 행, 열, 3 * 3 씩 계산
    go_stop = True
    if go_stop :
        for i in range(9):
            print(sum(inp[i]))
            if sum(inp[i]) != t_sum :
                go_stop = False
                break

    if go_stop :
        for i in range(9):
            tmp = 0
            for j in range(9):
                tmp += inp[j][i]
            if tmp != t_sum:
                go_stop = False
                break
            print(tmp)
    s = 0
    for i in range(3, 9+1, 3):
        print(s, i)
        t_33 = 0
        for j in range(s, i):
            for k in range(s, i):
                print(j, k)
                t_33 += inp[j][k]
        if t_33 != t_sum:
            go_stop = False
            break
        print('--')
        s = i
    if go_stop:
        answer = 'YES'
    else:
        answer = 'NO'
    return answer

#N = 5
inp = [
    [1, 4, 3, 6, 2, 8, 5, 7, 9],
    [5, 7, 2, 1, 3, 9, 4, 6, 8],
    [9, 8, 6, 7, 5, 4, 2, 3, 1],
    [3, 9, 1, 5, 4, 2, 7, 8, 6],
    [4, 6, 8, 9, 1, 7, 3, 5, 2],
    [7, 2, 5, 8, 6, 3, 9, 1, 4],
    [2, 3, 7, 4, 8, 1, 6, 9, 5],
    [6, 1, 9, 2, 7, 5, 8, 4, 3],
    [8, 5, 4, 3, 9, 6, 1, 2, 7]
]
re = solution()
print(re)
#=>