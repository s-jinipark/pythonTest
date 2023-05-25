
from collections import deque

# 프로그래머스 스타일 로 ...
def solution(N,  inp):
    answer = 0

    ans_str = ''
    qu = deque(inp)   # 생성 시 ()
    print(qu)    # deque([2, 4, 5, 1, 3])

    cnt = 0
    while cnt < N :

        print(qu[0], qu[-1])
        tmp = 0
        tmp_d = ''
        prev = -1

        if qu[0] < qu[-1] and qu[-1] > prev:
            tmp = qu.popleft()
            tmp_d = 'L'
        elif qu[0] > qu[-1] and qu[0] > prev:
            tmp = qu.pop()
            tmp_d = 'R'
        else:
            break

        if prev == -1 :
            prev = tmp
            answer += 1
            ans_str += tmp_d

        else :
            if prev + 1 == tmp :
                answer += 1
                ans_str += tmp_d
            else :
                break
        cnt += 1

        print(ans_str)

    return answer

N = 5

inp = [2, 4, 5, 1, 3]

re = solution(N, inp)
print('re :', re)
#=> LRLL 답인데 , LRRL 나옴
print('==============================')

N = 10

inp = [3, 2, 10, 1, 5, 4, 7, 8, 9, 6]

re = solution(N, inp)
print('re :', re)
#=> XX
print('==============================')
