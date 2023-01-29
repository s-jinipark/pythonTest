
# 문제 003 > 구간 합 구하기 1
# (* 중요)

inp1 = "5 3"
suNo, quizNo = map(int, inp1.split())
print(suNo, quizNo)  # 데이터의 개수, 질의 개수

# 입력 받을 경우
#numbers = list(map(int, input().split()))
numbers = [5,4,3,2,1]
print(numbers)  # 구간 합을 구할 대상 배열

#prefix_sum = []
prefix_sum = [0]  # 0 을 하나 넣어 놔야 한다는 ..
tmp = 0
for i in numbers :
    tmp = tmp + i
    prefix_sum.append(tmp)

print(prefix_sum)

#구간을 입력 받는다
for i in range(quizNo):
    print(i+1, " /" , quizNo , "> ", end='')
    s, e = map(int, input().split())
    #print(s, e, " = ", prefix_sum[e-1]-prefix_sum[s-1])
    print(s, e, " = ", prefix_sum[e] - prefix_sum[s - 1])

'''
두 가지를 잘 못 생각함
1. 처음에 prefix_sum[e-1]-prefix_sum[s-1] 로 했음
   5 5 가 들어 왔을 경우를 생각하면, 
   prefix_sum[e] - prefix_sum[s-1]
2.처음에 prefix_sum = [] 로 선언
  1 1 일 경우 s-1 해야 되니,
  prefix_sum = [0] 로 해야 ...
  (1,2 번 연관 있는 듯..)
'''
