def solution(s):
    answer = True

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    #print('Hello Python')

    print(s.lower())
    s = s.lower()
    p_cnt = 0
    y_cnt = 0
    for i in s :
        if i == 'p' :
            p_cnt += 1
        elif i == 'y' :
            y_cnt += 1
    print(p_cnt, y_cnt)

    if p_cnt + y_cnt == 0:
        return True
    if p_cnt == y_cnt :
        return True
    else :
        return  False
    #return True

#s = "pPoooyY"
s = "Pyy"

re = solution(s)
print(re)

print("====================")
