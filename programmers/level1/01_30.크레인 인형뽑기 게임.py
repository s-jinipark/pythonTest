def solution(board, moves):
    answer = 0
    bk = []

    for i in moves:
        print(i)
        # 열에서 가장 위 의 것 탐색
        for j in range(len(board)) :  # N X N 이라 함
            if board[j][i-1] > 0 :  # 열 고정이라는 점
                #print('>', board[j][i-1])
                #bk.append( board[j][i-1])
                # 기존에 들어 있는 거 확인
                if len(bk) >0 :  # 비어 있지 않다면 (비교하는 부분이 있음)
                    print(bk[-1], board[j][i - 1])
                    if bk[-1] == board[j][i - 1] :
                        bk.pop()  # 꺼내 버림
                        board[j][i - 1] = 0  # 0 셋팅은 해 줘야지..
                        answer += 1
                        break
                    print(bk[-1], board[j][i - 1])
                bk.append(board[j][i - 1])
                board[j][i - 1] = 0
                print(bk)
                break
    answer *= 2  # 사라진 인형 갯수니까
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

re = solution(board, moves)
print(re)

print("====================")

