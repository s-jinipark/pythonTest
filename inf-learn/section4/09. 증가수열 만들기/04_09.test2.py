

# 프로그래머스 스타일 로 ...
def solution(N,  inp):
    answer = 0
    # LT, RT 활용해서...
    lt = 0
    rt = N-1
    last_val = 0
    res = ''
    tmp = []  # 이것의 용도?
    while lt <= rt :  # < 로 생각했는데, <=
        if inp[lt] > last_val :
            tmp.append((inp[lt], 'L'))  # 여기서 튜플로 넣는 건 생각 못해봄
        if inp[rt] > last_val :
            tmp.append((inp[rt], 'R'))
        tmp.sort()
        if len(tmp) == 0:
            break
        else:
            res += tmp[0][1]
            last_val = tmp[0][0]
            if tmp[0][1] == 'L' :
                lt += 1
            else :
                rt -= 1
        tmp.clear()
    print(res)

    # 기존거는 lt , rt 중 어떤게 크냐 를 판단하면서
    # 이전 값보다 큰지도 판단해야 함
    # deque 를 쓰면 일부 cover 가 되나,
    # lt, rt 중 작은 값을 뽑았는데(lt 라고 가정), 이전 값보다 작을 경우
    # 반대쪽(rt)을 또 선택해야 해서.. 꼬임
    #
    # while lt < rt :
    #     연습 = 0
    #     if inp[lt] > inp[rt]  :
    #         연습 = inp[rt]
    #         rt -=1
    #     elif inp[lt] < inp[rt]:
    #         연습 = inp[rt]

    return answer

N = 5

inp = [2, 4, 5, 1, 3]

re = solution(N, inp)
print('re :', re)
#=>
print('==============================')

N = 10

inp = [3, 2, 10, 1, 5, 4, 7, 8, 9, 6]

re = solution(N, inp)
print('re :', re)
#=> XX
print('==============================')
