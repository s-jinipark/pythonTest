
def solution(food):
    answer = ''
    answer = '0'
    for i in range(len(food)-1, 0, -1):
        print(i, food[i])
        tmp = food[i]//2
        for j in range(tmp):
            answer = str(i) + answer + str(i)

    return answer

food = [1, 3, 4, 6]

re = solution(food)
print(re)

