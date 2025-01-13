
def solution(n, lost, reserve):
    answer = 0
    answer = n - len(lost)
    save = []
    lost.sort()  
    reserve.sort()
    # 자기 자신 구제
    for i in range(len(lost)):
        print(lost[i])
        for j in range(len(reserve)):
            if lost[i] == reserve[j] :
                save.append(lost[i])
                lost[i] = 0  # 0 으로 셋팅
                reserve[j] = 0

    # 남의 거 빌림
    for i in range(len(lost)):
        #print(l[i])
        if lost[i] == 0 :
            continue
        for j in range(len(reserve)):
            if reserve[j] == 0 :
                continue
            # -1 번호가 있는지 check ? 0보다 큰 경우 대상.
            if lost[i] > 1 and (lost[i]-1) == reserve[j] :
                save.append(lost[i])
                lost[i] = 0  # 0 으로 셋팅
                reserve[j] = 0
                break
            # +1 번호 체크한다
            if  (lost[i]+1) == reserve[j] :
                save.append(lost[i])
                lost[i] = 0  # 0 으로 셋팅
                reserve[j] = 0
                break
    print(reserve)
    print(save)
    answer += len(save)
    return answer

# n = 5
# l = [2,4]	
# r = [1,3,5]
n = 3
l = [3]	
r = [1]
an = solution(n, l, r)
print("=====")
print(an)