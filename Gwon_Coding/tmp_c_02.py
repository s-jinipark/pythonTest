

def dfs(num, org_n):
    q = "\"재귀함수가 뭔가요?\""
    a1 = "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어."
    a2 = "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지."
    a3 = "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\""
    c1 = "라고 답변하였지."

    pf = "____" * (org_n - num)

    if num == 0 :
        #print("맨 안")
        print(pf + q)
        print(pf +"\"재귀함수는 자기 자신을 호출하는 함수라네\"")
        print(pf +c1)
        return

    #print("전")
    print(pf +q)
    print(pf +a1)
    print(pf +a2)
    print(pf +a3)
    dfs(num-1, org_n)
    #print("후")
    print(pf +c1)

num = 2

print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
dfs(num, num)
