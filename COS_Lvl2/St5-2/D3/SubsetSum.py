w = []
check = []
W = 0
answer = 0

def subset(i, sumValue):
    global answer
    if sumValue > W:
        return

    if sumValue == W:
        answer += 1
    elif i <len(w)-1:
        subset(i+1, sumValue)
        # 1차로 적은 답

def solution(product, K):
    global w, check, W, total, answer
    answer = 0  # global 변수로 사용한 값 다른 샘플을위해 초기화
    w = product
    W = K
    check = [False for i in range(len(product))]
    subset(-1, 0)


product = [ 2, 1, 3, 5, 4, 6]
sumValue = 10
solution(product, sumValue)
print(answer)     # 5

product = [ 2, 10, 13, 17, 22, 42]
sumValue = 52
solution(product, sumValue)
print(answer)    # 2


