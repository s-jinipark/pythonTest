# 다음과 같이 import를 사용할 수 있습니다.
# import math

def DFS(L, chk):
    global  minVal
    if L == K :
        print(res)
        cha = max(res) -min(res)
        if minVal > cha:
            minVal = cha
        return
    else:
        for i in range(len(arr)):
            if chk[i] == 0 :
                res[L] = arr[i]
                chk[i] = 1
                DFS(L+1, chk)
                chk[i] = 0

def solution(arr, K):
    # 여기에 코드를 작성해주세요.
    answer = 0

    chk = [0] * len(arr)
    # DFS L: K , 가지수 : arr 수
    DFS(0, chk)

    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
arr = [9, 11, 9, 6, 4, 19]
K = 4

res = [0] * K
minVal = 2147000000

ret = solution(arr, K)
print(minVal)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")

'''
문제 설명
자연수가 들어있는 리스트에서 숫자 K개를 선택하려 합니다. 
이때, 선택한 숫자 중 가장 큰 수와 가장 작은 수의 차이가 최소가 되도록 해야합니다.

예를 들어 리스트에 들어있는 숫자가 [9, 11, 9, 6, 4, 19] 이고, K = 4 라면

ㆍ 숫자 4개를 [9, 11, 9, 6]로 뽑으면 (가장 큰 수 - 가장 작은 수) = (11 - 6) = 5가 됩니다.
ㆍ [9, 9, 6, 4] 와 같이 숫자를 뽑아도 (가장 큰 수 - 가장 작은 수) = (9 - 4) = 5가 됩니다.
그러나 가장 큰 수와 가장 작은 수의 차이가 5보다 작아지도록 숫자 4개를 선택하는 방법은 없습니다.

자연수가 들어있는 리스트 arr, 선택해야 하는 숫자 개수 K가 매개변수로 주어질 때, 
선택한 숫자중 가장 큰 수와 가장 작은 수의 차이가 최소가 되록 arr에서 숫자 K개를 선택했을 때, 
그때의 가장 큰 수와 가장 작은 수의 차이를 return 하도록 solution 함수를 완성해주세요.

매개변수 설명
자연수가 들어있는 리스트 arr, 선택해야 하는 숫자 개수 K가 solution 함수의 매개변수로 주어집니다.

ㆍ arr 리스트의 길이는 5 이상 1,000 이하입니다.
ㆍ arr의 원소는 1 이상 10,000 이하인 자연수입니다.
ㆍ K 는 4 이상 50 이하인 자연수입니다.

return값 설명
선택한 숫자중 가장 큰 수와 가장 작은 수의 차이가 최소가 되도록 arr에서 숫자 K개를 선택했을 때, 
그때의 가장 큰 수와 가장 작은 수의 차이를 return 해주세요.

예제
arr	                    K	return
[9, 11, 9, 6, 4, 19]	4	5

'''