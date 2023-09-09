def func_a(n, matrix):
    for i in range(n):
        temp = matrix[i][0]
        #print(temp)
        for j in range(n - 1):
            matrix[i][j] = matrix[i][j+1]
        matrix[i][n - 1] = temp

def func_b(n, matrix):
    for i in range(n):
        temp = matrix[i][n - 1]
        for j in range(n - 1, 0, -1):
            matrix[i][j] = matrix[i][j-1]
        matrix[i][0] = temp

def func_c(n, matrix):
    for j in range(n):
        temp = matrix[0][j]
        for i in range(n - 1):
            matrix[i][j] = matrix[i+1][j]
        matrix[n - 1][j] = temp

def func_d(n, matrix):
    for j in range(n):
        temp = matrix[n - 1][j]
        print(temp)
        for i in range(n - 1, 0, -1):
            matrix[i][j] = matrix[i-1][j]
        matrix[0][j] = temp

def solution(n, matrix, direction):
    for dir in direction:
        if dir == "left":
            func_a(n, matrix)
            print(matrix)
        elif dir == "right":
            func_b(n, matrix)
            print(matrix)
        elif dir == "up":
            func_c(n, matrix)
        elif dir == "down":
            func_d(n, matrix)
            print(matrix)

    return matrix

'''

'''
n =3
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
direction = ["left", "down", "right"]
an = solution(n, matrix, direction)
print(an)