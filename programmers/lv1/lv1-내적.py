
def solution(a, b):
    #answer = 1234567890
    answer = 0

    #print(len(a))
    for i in a:
        print(a[i-1])

    print("-----")

    for j in range(len(a)):
        print(a[j])
        answer += a[j]*b[j]

    return answer

#a = [1,2,3,4]	
#b = [-3,-1,0,2]
a = [-1,0,1]	
b = [1,0,-1]
an = solution(a, b)
print("=====")
print(an)