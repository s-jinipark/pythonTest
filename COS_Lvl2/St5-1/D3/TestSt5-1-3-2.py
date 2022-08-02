
def adjacent(x) :
    for i in range(x):
        #print(row)
        if row[x] == row[i] or abs(row[x] - row[i]) == x -i :
            return False
    return True

def dfs(x) :
    global  result

    if x == N :
        result += 1
    else :
        # 각 행에 퀸 놓기
        for i in range(N) :  # i 는 열번호 0 부터 N 전까지 옮겨 가면서 유망한 곳 찾기
            row[x] = i  # [x, i] 에 퀸을 놓겠다
            print(row, x, i , adjacent(x))
            if adjacent(x) :
                print("call " , x+1)
                dfs(x+1)
            #print(row, x, i, adjacent(x))
        #print("-----")

N = 3
row = [0] * 3
result = 0
#print(row)
dfs(0)
print(result)

'''
https://kom-story.tistory.com/348

https://sso-feeling.tistory.com/415?category=913126

N = 2 를 테스트 해보면 
[0, 0] 0 0 True     # 0 0 에 퀸을 놓는다
call  1             # 놓을 데가 없으니 다음 칸
[0, 0] 1 0 False    # 다음 칸의 0 (1,0)
[0, 1] 1 1 False    # 다음 칸의 1 (1,1)
[1, 1] 0 1 True     # 아까 0 0 다은으로 0 1 로 간다
call  1             # 놓을 데가 없으니 다음 칸
[1, 0] 1 0 False    # 다시 반복 (1,0)
[1, 1] 1 1 False    # 다시 반복 (1,1)

'''