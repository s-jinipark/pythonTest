# 다음과 같이 import를 사용할 수 있습니다.
# import math

##### 재차 연습

def solution(arr, K):
    # 여기에 코드를 작성해주세요.
    answer = 0
    arr.sort()
    print(arr)
    for i in range(0, len(arr) - K + 1):
        print(i, i + K - 1)
        #print(arr[i + K - 1] - arr[i])

    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
arr = [9, 11, 9, 6, 4, 19]
K = 4

#res = [0] * K
#minVal = 2147000000

ret = solution(arr, K)
#print(minVal)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")

