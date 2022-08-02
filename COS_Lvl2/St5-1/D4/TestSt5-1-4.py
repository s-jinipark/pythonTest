answer = 0
N = 0

def dfs(idx, total, target_val) :
    global answer
    if (idx == N and target_val == total):
        answer += 1
        return
    if (idx == N):
        return
    #print(idx, total + arr[idx])
    #print(total + arr[idx], end=' ')
    dfs(idx+1, total + arr[idx], target_val)
    #print(total + arr[idx], end=' ')
    dfs(idx+1, total - arr[idx], target_val)
    #print( arr[idx], end=' ')
def solution(numbers, target):
    #answer = 0
    global arr, N
    arr = numbers
    N = len(numbers)

    print(numbers, target)

    dfs(0, 0, target)
    return answer


# 각 샘플 하나씩 주식 해제하고 실행한 후 확인하세요.
#sample 1
numbers = [1,1,1,1,1]
target = 3

res = solution(numbers,target)
print(res)

#sample 2
numbers = [1,1,1]
target = 1

#sample 3
# numbers = [2, 2, 2, 2, 2]
# target = 10

res = solution(numbers,target)
print(res)
