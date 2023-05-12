
# n개의 음이 아닌 정수가 있습니다. 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다.
# 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3

# numbers = [1,1,1]
#
# target = 1
#
# tot = 0
#
# def dfs(n, tot, trgt):
#     l_num = len(numbers)
#     if n == l_num: # 종료 조건
#         print(numbers)
#         print('tot > ' , tot)
#         return
#     print('--')
#
#     dfs(n+1, tot + numbers[n], trgt)
#     dfs(n+1, tot - numbers[n], trgt)
#
#     #print(tot)
#
# dfs(0, 0, target)

answer = 0
N = 0

def dfs(idx, total, targetValue):
    print("dfs (", idx, total, target, ")")
    global answer
    if(idx== N and target == total):
        print(" 종료 dfs (", idx, total, target, ")")
        answer += 1
        return
    if(idx == N):
        return

    dfs(idx+1,total+arr[idx], targetValue)
    dfs(idx+1,total-arr[idx], targetValue)


def solution(numbers, target):
    global arr, N
    arr = numbers
    N = len(numbers)

    print(numbers, target)
    dfs(0, 0, target)

    return answer


# 각 샘플 하나씩 주식 해제하고 실행한 후 확인하세요.
#sample 1
# numbers = [1,1,1,1,1]
# target = 3

#sample 2
numbers = [1,1,1]
target = 1

res = solution(numbers,target)
print(res)




