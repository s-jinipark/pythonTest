
def solution(n, photo):
    board = []

    for p in photo:
        if p in board:
            continue
        elif len(board) < n:
            board.append(p)
        else:
            board.pop(0)
            board.append(p )

    return sorted(board)

'''

'''
n = 3
photo = [1,2,1,5,5,4,3]

an = solution(n, photo)
print(an)