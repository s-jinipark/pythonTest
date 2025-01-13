
# 두 개 뽑아서 더하기

def solution(numbers):
    #print(numbers)
    answer = []
    for i in range(0, len(numbers)-1):
        for j in range(i+1, len(numbers)):
            #print(numbers[i] + numbers[j] )
            answer.append(numbers[i] + numbers[j])
    b = set(answer) 
    answer = list(b)
    answer.sort()
    print(answer)
    return answer

a = [2,1,3,4,1]
solution(a)

b = [5,0,2,7]
solution(b)