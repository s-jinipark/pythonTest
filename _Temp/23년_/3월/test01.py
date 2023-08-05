
def solution(seats):

    for i in range(len(seats) - 1, 0, -1):
        for j in range(0, i):
            print(i, j , '-', j, 1, j+1 , 1)
            if seats[j][1] > seats[j + 1][1]:   # 열번호 우선
                temp = seats[j]
                seats[j] = list(seats[j + 1])
                seats[j + 1] = temp

            elif seats[j][1] == seats[j + 1][1] :
                if  abs(15 - seats[j][0]) > abs(15 - seats[j + 1][0] ) :
                    temp = seats[j]
                    seats[j] = list(seats[j + 1])
                    seats[j + 1] = temp
    print(seats)
    return ''
    #return list(seats)


seats = [[15,15],[10,10],[5,5],[30,15],[1,15]]

an = solution(seats)
print(an)