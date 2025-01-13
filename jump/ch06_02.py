
# 3과 5의 배수 합하기

def ThreeFive(n):
    result = 0
    for i in range(1,n):
        if i % 3 == 0 or i % 5 == 0 :
            result += i
    return result


result= ThreeFive(1000)
print(result)
