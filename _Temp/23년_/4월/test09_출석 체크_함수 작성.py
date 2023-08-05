
# 출석 체크

def solution(names):
    answer = []

    temp = set()
    for n in names:
        temp.add(n)

    #answer = (list)temp  # 으악, 안 됨.. 자바 랑 헷갈림
    answer = list(temp)
    answer.sort()
    print(answer)

    return answer

'''

'''


names	 = ["Amy", "Carol", "Bob", "Amy"]

an = solution(names	)
print('an = ', an)


'''
[처음 짠]
def solution(names):
    answer = []
    tmp = set()
    for n in names:
        tmp.add(n)
    #print(tmp)
    answer = list(tmp)
    answer.sort()
    return answer
'''