

def solution(sequence):
    n = len(sequence)
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            #print(i, j)
            if sequence[i] < sequence[j]:
                print(sequence[i] , sequence[j])
                #dp[i] = max(dp[i], dp[j])
                dp[j] = max(dp[i] , sequence[i])
    print(dp)
    return max(dp)


'''

'''
sequence = [1,4,3,3,5,1]

an = solution(sequence)
print(an)