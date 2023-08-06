
def solution(time):
    answer = 0
    '''
    "03:00 am" 이후, "06:30 am" 이전에
    기상해야 미라클모닝에 성공한 것으로 간주
    '''

    for t in time:
        print(t, t[:2], t[3:5], t[6:])
        tm = int(t[:2])
        mi = int(t[3:5])
        if t[6:] == 'am' :
            if (tm >=3 and tm < 6 ) :
                answer +=1
            elif (tm ==6 and mi <= 30 ):
                answer +=1

    return answer


time =["06:30 am", "07:00 am", "04:50 am"]

an = solution(time)
print('an = ', an)

