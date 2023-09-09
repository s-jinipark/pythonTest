
def solution(lottery, money):
    answer = 0

    for l in lottery :
        #print(l[0], l[1])
        # 길이 동일하다 했으니까
        tot = len(l[0])
        ok = 0
        for i in range(len(l[0])):
            print(l[0][i], l[1][i])
            if l[0][i] == l[1][i]:
                ok += 1
        if tot == ok :
            answer += money
        elif tot-1 == ok:
            answer += int(money/2)

    return answer


lottery = [["apple", "apple"], ["dog", "dot"], ["love", "like"]]
money = 1000

an = solution(lottery, money)
print(an)