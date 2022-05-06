def func_a(string, length):
    padZero = ""
    #padSize = @@@
    padSize = length - len(string)

    for i in range(padSize):
        padZero += "0"
    return padZero + string

def solution(binaryA, binaryB):
    max_length = max(len(binaryA), len(binaryB))
    # binaryA = func_a(binaryA, max_length)
    # binaryB = func_a(binaryB, max_length)
    # 주의 @@@ 표시 같은 거 없어서 몰랐음
    if max_length > len(binaryA) :
        binaryA = func_a(binaryA, max_length)
    if max_length > len(binaryB) :
        binaryB = func_a(binaryB, max_length)

    hamming_distance = 0
    for i in range(max_length):
        #if @@@:
        if binaryA[i]  != binaryB[i]:
            hamming_distance += 1
    return hamming_distance

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
binaryA = "10010"
binaryB = "110"
ret = solution(binaryA, binaryB)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("Solution: return value of the function is", ret, ".")