#다음과 같이 import를 사용할 수 있습니다.
#import math

def func_a(n, garden):
    rtn = []
    for i in range(n):
        for j in range(n):
            if garden[i][j] == 1 :
                rtn.append([i, j])
    return rtn

def func_b(n, lst_a):
    pos_x = [-1,1,0,0]
    pos_y = [0,0,-1,1]
    rtn = []
    for lst in lst_a :
        print(lst)
        tmp_x = lst[0]
        tmp_y = lst[1]
        for i in range(4) :  # 상하좌우니까 4
            if 0 <= tmp_x + pos_x[i] < n and 0 <= tmp_y + pos_y[i] < n :
                rtn.append([tmp_x + pos_x[i], tmp_y + pos_y[i]])
    return rtn

def solution(n, garden):
    #여기에 코드를 작성해주세요.
    answer = 0

    # 상하 좌우 를 차례로 보면 될 것 같은데
    # 대상자 .. 즉 그날의 대상인지 여부를 어떻게 구분하지
    # 한번 거쳐가서 1로 바뀐 애를 또 바꾸면 안되자너..

    # 가장 먼저 1 의 위치 -> 행, 열 좌표
    # 큐에 넣고 하는 거 같은데.
    # 1) 먼저 1을 찾아서 큐에 '상하좌우' 를 넣는다
    # 2) 이걸 빼서 1로 셋팅
    # 3) 1 이 아닌 경우 있는지 chk
    flag = True
    cnt = 0
    while flag :
        lst_a = func_a(n, garden)
        print(lst_a)

        # 상하 좌우 가져 오기
        lst_b = func_b(n, lst_a)
        print(lst_b)

        # 1 로 셋팅
        for lst in lst_b :
            garden[lst[0]][lst[1]] = 1
            #print(lst[0], lst[1])
        print(garden)

        flag = False
        # 0 있는지 검사
        for i in range(n):
            for j in range(n):
                if garden[i][j] == 0 :
                    flag = True
                    cnt += 1    # 여기서 count 해줌
                    break


    answer = cnt
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
n1 = 3
garden1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
ret1 = solution(n1, garden1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

n2 = 2
garden2 = [[1, 1], [1, 1]]
ret2 = solution(n2, garden2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")