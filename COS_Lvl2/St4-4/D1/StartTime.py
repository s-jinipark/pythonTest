def solution(numlist):
    answer = 0
    # 코드를 작성하세요.

    n = len(numlist)
    sum_list = [0] * n
    print(sum_list)

    flag_out = True
    cnt = 0
    while cnt < 10 : #flag_out :
        for i in range(n) :
            sum_list[i] += numlist[i]
        print(sum_list)
        # 점검
        # index 0 이랑 나머지가 같으면 되자너
        test = sum_list[0]
        flag_in = True
        for j in range(1, n):
            if test != sum_list[j] :
                flag_in = False
                break
        if flag_in :
            flag_out = False
        cnt += 1

    return answer

numlist = [6, 8, 5, 12]
res = solution(numlist)
print(res)

# numlist = [4, 7, 20, 12]
# res = solution(numlist)
# print(res)

