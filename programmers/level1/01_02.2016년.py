def solution(a, b):
    answer = ''
    # 1월 1일은 금요일
    last_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
    tot_days = 0
    for i in range(a-1):
        #print(i)
        tot_days += last_days[i]
    tot_days += b
    print(tot_days, tot_days % 7)
    tmp_days = tot_days % 7  + 5  -1 # 1월 1일의 ind 는 5
    print(tmp_days )
    if tmp_days > 6 :
        tmp_days %= 6
    print(days[tmp_days-1])
    return answer

a = 5
b = 24

re = solution(a, b)
print(re)

print("====================")
