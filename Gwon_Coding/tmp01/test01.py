

#num = int(input())
#print(num)
num = 4

# 반복되는 부분 파악
def recur(n, org) :
    q = "\"재귀함수가 뭔가요?\""
    a1 = "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어."
    a2 = "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지."
    a3 = "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\""

    b1 = "\"재귀함수는 자기 자신을 호출하는 함수라네\""

    c1 = "라고 답변하였지."

    tmp = ''
    for i in range(org - n):
        tmp += '____'

    if n == 0:
        print(tmp+q)
        print(tmp+b1)
        print(tmp+c1)
    #elif n == 0 :
    #    return
    else :
        print(tmp+q)
        print(tmp+a1)
        print(tmp+a2)
        print(tmp+a3)
        recur(n-1, org)
        print(tmp+c1)

print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")

recur(num, num)
