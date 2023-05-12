
# 1차 시도는 틀림

def solution(numbers, hand):
    answer = ''
    L_last = 10
    R_last = 10

    for n in numbers :
        #print(n)

        print(L_last, R_last)
        if n in [3, 6, 9] :
            print(n, "R")
            R_last = n
            answer += "R"
        elif n  in [1, 4, 7] :
            print(n, "L")
            L_last = n
            answer += "L"
        elif n  in [2, 5, 8, 0] :
            # if n == 0:
            #     n = 11
            print(n, "&")
            print(L_last, R_last)
            L_cur = abs(L_last - n)
            R_cur = abs(R_last - n)
            # [초기 생각] 빼기(-) 한 뒤 절대값으로 비교해서 적은 값을 취하면 될 듯
            print(L_cur, R_cur, abs(L_cur), abs(R_cur))
            # [2] 가운데를 찍은 상태라면, 달라짐
            if L_last in [2,5,8,0]:
                print(">>", distance_LR(L_last, n))
                L_cur = distance_LR(L_last, n)
            if R_last in [2,5,8,0]:
                print(">>", distance_LR(R_last, n))
                R_cur = distance_LR(L_last, n)

            if L_cur > R_cur :
                R_last = n
                print(n, "R")
                answer += "R"
            elif L_cur < R_cur :
                L_last = n
                print(n, "L")
                answer += "L"
            else :  # 같다는 얘기지
                if hand == "right" :
                    R_last = n
                    print(n, "R")
                    answer += "R"
                else :
                    L_last = n
                    print(n, "L")
                    answer += "L"

    return answer

def distance_LR(last, cur):
    res = 0
    if cur == 0 :
        cur = 11
    res = abs(last - cur)//3
    return res

#numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
#hand = "right"

numbers =[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"

re = solution(numbers, hand)
print(re)
