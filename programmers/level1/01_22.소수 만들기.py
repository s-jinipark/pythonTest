def isPrime(n):
    for i in range(2, n):
        if n % i == 0 :
            return False
    return True

def solution(arr):
    answer = 0

    # 문제에서 3개의 수 라고 했으니 ..
    for i in range(len(arr)-2):
        for j in range(i+1, len(arr)-1):
            for k in range(j+1, len(arr)):
                #if i != j and j != k and k != i :
                sum = 0
                print(i, j, k)
                sum = arr[i] + arr[j] + arr[k]
                #print(sum, isPrime(sum))
                if isPrime(sum):
                    answer += 1

    return answer



#arr = [1,2,3,4]
arr = [1,2,7,6,4]

re = solution(arr)
print(re)

print("====================")
