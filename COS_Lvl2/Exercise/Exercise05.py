
# N과 M(1)
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
#   . 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

#N, M = map(int, input().split())
#N, M = 3,1
N, M = 4,2

s = []   # 수열을 저장하기 위한 리스트

def dfs():
  if len(s) == M :  # 뽑는 갯수와 맞춘다
    #print('**')
    print(s)
    return

  for i in range(1, N+1) :  # 1부터 카드 뽑는 상황이라...
    if i not in s :  # 리스트에 없을 경우
      s.append(i)
      dfs()  # 현재 s=[1]인 상태에서 다음숫자를 넣기위하여 가지치기하기(재귀함수)
      s.pop()

dfs()

#print(s)

########################################
# N과 M (2)
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
#  . 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
#  . 고른 수열은 오름차순이어야 한다.
# 위(15649번과) 거의 동일하지만 이 문제에서는 [1,2], [2,1]과 같은 경우는 중복되는 경우로 보고 [1,2]만 출력해야 한다.

# 이건 combination 으로 했는데 -> 걍 암기 ?
# 문제를 읽어보면 구분이 확 되지는 않음

# 여기 참조 : https://jiwon-coding.tistory.com/22?category=882771

print('-------------------------')
#N, M = 3,1
N, M = 4,2

s = []   # 수열을 저장하기 위한 리스트

def dfs(start):
  if len(s) == M :
    print(' '.join(map(str, s)))
    return

  for i in range(start, N+1) :  # ** start 부터 4까지의 카드
    if i not in s :
      s.append(i)
      #dfs(i+1)  # ** ?? 이거를 하면 if 가 없어도 된다네 ..
      dfs(i)
      s.pop()

dfs(1)


print('-------------------------')

# 이 문제는 15649번과 동일하지만, 중복을 허용하기 떄문에, 10번의 for문에서 중복을 확인하는 if문이 삭제되었다.

#N, M = 3,1
N, M = 4,2

s = []

def dfs() :
  if len(s) == M :
    print(s)
    return

  for i in range(1, N+1):
    s.append(i)
    dfs()
    s.pop()

dfs()


print('-------------------------')

# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
#   . 1부터 N까지 자연수 중에서 M개를 고른 수열
#   . 같은 수를 여러 번 골라도 된다.
#   . 고른 수열은 비내림차순이어야 한다.
#     .. 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.

# 계속 커지는 스타일 ???
# [2,1] 같은 게 안되고 [2,2] 부터 시작
# => 이거는 문제 스타일을 암기해야 할 듯

#N, M = map(int, input().split())
#N, M = 3,1
N, M = 4,2

s = []

def dfs(start):
  if len(s) == M :
    print(s)
    return

  for i in range(start, N+1) :
    s.append(i)
    dfs(i)
    s.pop()

dfs(1)





