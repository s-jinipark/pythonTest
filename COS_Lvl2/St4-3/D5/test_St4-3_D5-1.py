def solution(bishops):
    #여기에 코드를 작성해주세요.

    answer = 0
    a = [[0] * 9 for _ in range(9)]
    #print(a)
    # 특이하게 X 가 알파벳
    for bis in bishops :
        print(bis)
        x = ord(bis[0]) - ord('A') +1
        y = int(bis[1])
        print(x, y)

    # 다시 오는 걸로 ...


    return answer


#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
bishops1 = ["D5"]
ret1 = solution(bishops1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

bishops2 = ["D5","E8", "G2"]
ret2 = solution(bishops2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")