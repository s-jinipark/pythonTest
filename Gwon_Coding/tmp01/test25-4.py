
# n개의 음이 아닌 정수가 있습니다. 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다.
# 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3

numbers = [1,1,1]

target = 1

tot = 0

N = len(numbers)

# DFS , 스택 이용

def dfs(n):
    answer = 0
    stk = []
    stk.append([numbers[0], 0])
    stk.append([-1 * numbers[0], 0])

    while len(stk) > 0 :
        temp, idx = stk.pop()
        idx += 1
        print('[', temp, ',', idx, '] pop')
        if idx < N :
            stk.append([temp+numbers[idx], idx])
            stk.append([temp-numbers[idx], idx])
            print(stk)
        else :
            if temp == target :
                print('>', stk)
                answer += 1
    return answer

ans = dfs(0)
print(ans)

# 재귀를 쓰지 않으면,
# DFS 나 BFS 나 똑같다는 ... ㅠ.ㅠ

