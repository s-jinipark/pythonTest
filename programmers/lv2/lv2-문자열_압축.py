
def solution(s):
    answer = 0
    tmp_len = len(s)
    min_len = 1001
    for i in range(1, tmp_len+1) :
        print(i)
        #print(s[0:0+i])
        pos =0
        pre = ""
        cur = ""
        cnt = 1
        output = ""
        while pos < tmp_len :
            print(s[pos:pos+i])
            cur = s[pos:pos+i]
            pos += i
            if pre == cur :
                print(">", cur)
                cnt = cnt + 1
                print(cnt)
            else :
                if pre != "":  # 맨 앞이 아니라면
                    tmp_num = ""
                    if cnt == 1 :
                        tmp_num = ""
                    else :
                        tmp_num = str(cnt)
                    output += tmp_num + pre
                cnt = 1    
            pre = cur
        # 마지막
        tmp_num = ""
        if cnt == 1 :
            tmp_num = ""
        else :
            tmp_num = str(cnt)
        output += tmp_num + pre
        print("=>" , output)
        if min_len > len(output) :
            min_len = len(output)
    answer = min_len
    return answer


s = "aabbaccc"
an = solution(s )
print("=====")
print(an)