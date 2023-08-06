
# 전교1등_빈칸채우기

def solution(grade):
    total_score = []

    def func_a(param):
        ret = 0
        for i in range(len(total_score)):
            if total_score[i] == param :
                ret += 1
        return ret


    def func_b(grade):
        for i in range(len(grade)):
            total_score.append(grade[i][0] + grade[i][1])


    def func_c():
        ret = 0
        for i in range(len(total_score)):
            if total_score[i] > ret :
                ret = total_score[i]
        return ret

    func_b(grade)
    max_num = func_c()
    answer = func_a(max_num)

    return answer


'''

'''

grade = [[90, 100], [100, 90], [60, 75]]

an = solution(grade)
print(an)