
def solution(a, b):
    answer = ''
    #days = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
    days = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    last_day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    culc_d = 0
    start_d = 5  # index 

    if a == 1 :
        culc_d = b
    else :
        for i in range(1, a):
            culc_d += last_day[i-1]
        culc_d += b

    print(culc_d)
    print(culc_d%7)
    if culc_d <= 7 :
        tmp = culc_d-1
    else :
        tmp = culc_d%7 -1
    answer = days[tmp]
    return answer

a = 2
b = 1
an = solution(a , b)
print("=====")
print(an)