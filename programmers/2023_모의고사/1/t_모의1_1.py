def solution(seats):
    for i in range(len(seats) - 1, 0, -1):
        for j in range(0, i):
            print(j, seats[j][1]  , seats[j + 1][1])  # 열 정렬
            if seats[j][1] > seats[j + 1][1]:
                temp = seats[j]
                seats[j] = list(seats[j + 1])
                seats[j + 1] = temp
                print(seats)
            elif seats[j][1] == seats[j + 1][1]:
                print(seats[j][1], '--', seats[j + 1][1])
                if abs(15-seats[j][0]) > abs(15-seats[j + 1][0]):
                    temp = seats[j]
                    seats[j] = list(seats[j + 1])
                    seats[j + 1] = temp
    print(seats)
    return list(seats)


seat = [[15,15], [10,10], [5,5], [30,15], [1,15]]

'''
열번호가 작은 좌석
열번호가 같다면 행 번호가 무대 중앙에 더 가까운 좌석
  - 15에 가까울 수록 ...
'''
solution(seat)
