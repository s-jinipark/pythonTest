
##### 격자판 회문수
def solution():
    answer = 0

    # 7 * 7 격자판
    for i in range(7):
        print(inp[i])
        start = 0
        end = 5
        while end <= 7 :
            tmp = []
            for j in range(start, end):
                #print(j, end=' ')
                tmp.append(inp[i][j])

            tmp2 = []
            for j in range(start, end):
                #print(j, end=' ')
                tmp2.append(inp[j][i])
            #print()
            #print(연습)
            # 회문수

            for k in range(2):
                #print(연습[k], 연습[4-k])
                if tmp[k] != tmp[4 - k] :
                    break
            else:
                print(tmp)
                answer += 1

            for l in range(2):
                #print(tmp2[l], tmp2[4-l])
                if tmp2[l] != tmp2[4 - l] :
                    break
            else:
                print(tmp2)
                answer +=1

            start +=1
            end += 1

    return answer

#N = 5
inp = [
    [2, 4, 1, 5, 3, 2, 6],
    [3, 5, 1, 8, 7, 1, 7],
    [8, 3, 2, 7, 1, 3, 8],
    [6, 1, 2, 3, 2, 1, 1],
    [1, 3, 1, 3, 5, 3, 2],
    [1, 1, 2, 5, 6, 5, 2],
    [1, 2, 2, 2, 2, 1, 5]
]
re = solution()
print(re)
#=>