
def solution(s):
    answer = -1

    pre = ""
    cur = "" 
    tmp_str = list(s)
    tmp_len = len(tmp_str)
    tmp_flag = True
    print(tmp_str)
    cnt = 0
    while cnt < tmp_len :
        tmp_len = len(tmp_str)
        #print(">", tmp_len)
        for i in range(tmp_len) :
            cur = tmp_str[i]
            if pre == cur : 
                #큰거부터 제거
                del tmp_str[i] 
                del tmp_str[i-1] 
                #tmp_len = len(tmp_str) # 셋팅 다시
                break  # 끝내고 다시
            else :
                pre = cur
            # if i == tmp_len-1 :  # 마지막
            print(i , "/", tmp_len-1)
        cnt += 1
        #tmp_flag = False # 여기까지 왔다면 다 돌은 것으로 판단

    print(tmp_str)
    if len(tmp_str) == 0 :
        answer = 1
    else :
        answer = 0
    # 문자 모두 제거 : 1 , 아닌 경우 0
    return answer


s = "baabaa"
#s = "cdcd"
an = solution(s )
print("=====")
print(an)