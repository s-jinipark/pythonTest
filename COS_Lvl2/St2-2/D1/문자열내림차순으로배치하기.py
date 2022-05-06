# 문자열 내림차순으로 배치하기

def solution(s):
    answer = ''
    tmp_list = list(s)
    print(tmp_list)

    for i in range(len(tmp_list)):
        for j in range(len(tmp_list)-1):
            if tmp_list[j] < tmp_list[j+1] :
                tmp = tmp_list[j+1]
                tmp_list[j+1] = tmp_list[j]
                tmp_list[j] = tmp

    for t in tmp_list :
        answer += t
    return answer

s = "Zbcdefg"        # "gfedcbZ"
res = solution(s)
print(res)

s = "TsBuacykd"     # "yuskdcaTB"
res = solution(s)
print(res)


