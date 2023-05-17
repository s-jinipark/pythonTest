
def solution(N, su_lst):
    answer = 0
    acc = 0   # 누적

    for s in su_lst:
        print(s)
        if s == 1 :
            answer += 1 + acc
            acc += 1
        else :
            acc = 0

    return answer

N = 10
su_lst = [1, 0, 1, 1, 1, 0, 0, 1, 1, 0]

re = solution(N, su_lst)
print(re)
print('====================')

