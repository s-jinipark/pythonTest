
# K번째수

def solution(array, commands):
    #print(array)
    #print(commands)
    answer = []
    for c in commands:
        #print(c[0], c[1], c[2])
        tmp = array[(c[0])-1:c[1]]
        #print(tmp.sort())  # 이렇게 하면 None 이 출력 됨 
        tmp.sort()
        #print(tmp)
        tmp2 = tmp.pop(c[2]-1)
        #print(tmp2)
        answer.append(tmp2)
  
    return answer

a = [1, 5, 2, 6, 3, 7, 4]
c = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
an = solution(a, c)
print(an)


