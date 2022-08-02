answer = 0
N = 0

def dfs(idx, total, targetValue):
    global answer
    if (idx == N and target == total):
        answer += 1
        return
    if (idx == N) :
        return
    dfs(idx+1, total+arr[idx], targetValue)
    dfs(idx+1, total-arr[idx], targetValue)


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

#sample 2
# numbers = [1,1,1]
# target = 1

#sample 3
# numbers = [2, 2, 2, 2, 2]
# target = 10

res = solution(numbers,target)
print(res)
