
# 창고 정리
def find_min_max():
    Min = min(inp)
    Max = max(inp)
    Min_idx = 0
    Max_idx = 0
    print(Min, Max)
    for i in range(len(inp)):
        if inp[i] == Min:
            Min_idx = i

        if inp[i]== Max:
            Max_idx = i

    print(Min_idx, Max_idx)
    return (Min_idx, Max_idx)

def solution():
    answer = 0

    # 가장 높은 곳이나 가장 낮은 곳이 여러곳이면 그 중 아무거나 선택하면 된다.
    for i in range(M):
        print(i, find_min_max())
        Min_idx, Max_idx = find_min_max()
        inp[Min_idx] += 1
        inp[Max_idx] -= 1

    Min_idx, Max_idx = find_min_max()
    print('>', inp[Max_idx]- inp[Min_idx])
    return answer

'''
강사는 매번 소팅해서..
맨 앞값과 맨 뒤값을 계산 (맨앞 +1 , 맨뒤 -1)
마지막에는 맨뒤 - 맨앞 계산
'''


L= 10   # 창고 가로의 길이

inp = [69, 42, 68, 76, 40, 87, 14, 65, 76, 81]

M = 50  # 높이 조정 횟수

re = solution()
print('re :', re)
#=>
print('==============================')

