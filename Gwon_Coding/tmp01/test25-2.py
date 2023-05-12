
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

def dfs(n, tot):

    print(n, tot)

    # 종료 조건
    if n == N :
        #print('---')
        #print(n, tot)
        if tot == target :
            print('---', tot)
        return

    dfs(n+1, tot + numbers[n])
    dfs(n+1, tot - numbers[n])


    #print(tot)

dfs(0, 0)


'''
여기 참조
https://velog.io/@ju_h2/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-level2-%ED%83%80%EA%B2%9F%EB%84%98%EB%B2%84-BFSDFS

'''
