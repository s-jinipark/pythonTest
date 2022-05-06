# K번째수

def solution(array, commands):
    answer = []

    for c in commands :
        #print(c)
        tmp = array[c[0]-1:c[1]]
        print(tmp)
        # 정렬
        tmp.sort()
        answer.append(tmp[c[2]-1])
    return answer



# main 부분
array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

res = solution(array, commands)  # [5, 6, 3]
print(res)


