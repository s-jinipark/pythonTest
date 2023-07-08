def solution(prices):
    INF = 1000000001;
    tmp = INF
    answer = -INF
    for price in prices:
        if tmp != INF:
            #answer = max(answer, 연습 - price)
            answer = max(answer, price - tmp)
        tmp = min(tmp, price)
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution 함수만 수정하세요.
prices1 = [1, 2, 3]
ret1 = solution(prices1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("Solution: return value of the function is", ret1, ".")

prices2 = [3, 1]
ret2 = solution(prices2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("Solution: return value of the function is", ret2, ".")