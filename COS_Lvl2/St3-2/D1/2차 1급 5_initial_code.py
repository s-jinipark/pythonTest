#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(arr):
    #여기에 코드를 작성해주세요.
    answer = 0
    max = 0
    pre = -1
    for a in arr :
        print(pre, a)
        #if a > pre and pre > 0 :
        if a > pre :
            answer += 1
        else :
            if max < answer :
                max = answer
            answer = 0
        pre = a
        print(answer)
    #return answer
    if max < 2 :
        max = 1
    else :
        max += 1  # 배열의 맨 앞 도 계산 해야 됨
    return max

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
arr = [3, 1, 2, 4, 5, 1, 2, 2, 3, 4]
ret = solution(arr)


#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")