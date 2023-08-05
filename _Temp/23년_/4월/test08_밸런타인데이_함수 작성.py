
# 밸런타인데이

def solution(dates):
    answer = 0

    sample = [1,2,4,8]

    for d in dates :
        d = d.replace('/','')
        print(d)
        flag = True
        for d2 in d:
            print(d2)
            if int(d2) not in sample:
                flag = False
                break
        if flag :
            answer += 1

    return answer

'''
2의 거듭제곱수
 1 -> 0 제곱
 2 -> 1 제곱
 4 -> 2
 8 -> 3
 
 1248 이면 된다는 거자너
'''


dates = ["2/14", "6/8", "10/13"]

an = solution(dates)
print('an = ', an)


'''
[처음 짠]
def solution(dates):
    answer = 0
    for i in range(len(dates)):
        #print(dates[i].replace('/',''))
        dates[i] = dates[i].replace('/', '')

    sample = '1248'

    for i in dates:
        tmp = 0
        for j in i :
            #print(j)
            if j in sample:
                tmp += 1
        if tmp == len(i):
            answer += 1
    return answer
'''