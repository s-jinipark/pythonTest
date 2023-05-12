def solution(n, lost, reserve):
    answer = 0
    # 먼저 lost 이면서, reserve 있을 경우 먼저
    for l in lost:
        print(l)
        if l in reserve:
            print(l)
            lost.remove(l)
            reserve.remove(l)

        # 그다음 적은거 찾고, 높은거 찾고
        if l-1 in reserve :
            print('>', l-1)
            lost.remove(l)
            reserve.remove(l-1)

        # 그다음 높은거 찾고
        elif l+1 in reserve :
            print('>>', l-1)
            lost.remove(l)
            reserve.remove(l+1)

    print(lost)
    print(reserve)

    return answer

n = 5
lost = [2,4]
reserve = [1,3,5]
re = solution(n, lost, reserve)
print(re)

print("====================")

''''
remove 하니까 한번 돌고 멈춰 버림
lost 2 개 일때 한번 돌고 remove 하니까 
1개로 줄어들고, 다음 돌게 없다고 생각하는 듯

=> save 라는 list 에 save 된 거 넣고 계산 해야 할 듯  
'''

def solution2(n, lost, reserve):
    answer = 0
    save = []
    # 먼저 lost 이면서, reserve 있을 경우 먼저
    for l in lost:
        print(l)
        if l in reserve:
            print(l)
            save.append(l)
            reserve.remove(l)

        # 그다음 적은거 찾고, 높은거 찾고
        if l-1 in reserve :
            print('>', l-1)
            save.append(l)
            reserve.remove(l-1)

        # 그다음 높은거 찾고
        elif l+1 in reserve :
            print('>>', l-1)
            save.append(l)
            reserve.remove(l+1)
    print(save)
    answer = n - len(lost) + len(save)
    return answer


lost2 = [2,4]
reserve2 = [1,3,5]
re2 = solution2(n, lost2, reserve2)
print(re2)
