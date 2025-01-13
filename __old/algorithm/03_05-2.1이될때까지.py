def solution(i1):
    answer = 0
    ilist1 = i1.split()
    n = int( ilist1[0] )
    k = int( ilist1[1] )
    count = 0

    while n > 1 :
        if n % k == 0 :
            n = n/k
        else :
            n -= 1
        count += 1

    return count



inp1 = "25 5"
#inp2 = ["3 1 2", "4 1 4", "2 2 2"]

print("----- -----")
print(solution(inp1))
print("----- -----")
inp1 = "25 3"
print(solution(inp1))

