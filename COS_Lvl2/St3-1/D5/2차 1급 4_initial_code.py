#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(arr, K):
    #여기에 코드를 작성해주세요.
    answer = 0
    # 답지 보고 코딩해봄
    n = len(arr)
    for i in range(0, n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if (arr[i]+arr[j]+arr[k]) % K == 0 :
                    print(arr[i], arr[j], arr[k])
                    answer += 1
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
arr = [1, 2, 3, 4, 5]
K = 3
ret = solution(arr, K)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")