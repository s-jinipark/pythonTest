def solution(i1, i2):
    answer = 0

    ilist1 = i1.split()
    print(ilist1)
    ilist2 = i2.split()
    print(ilist2)
    # sort
    ilist2.sort()
    print(ilist2)
    ilist2.sort(reverse=True)
    print(ilist2)

    for i in range(1,int(ilist1[1])+1):
        if i%(int(ilist1[2])+1) == 0 :  # 나누어 떨어지면.. 
                                        # 여기서는 3번 나오고 1번 나오는 식이니 4로 나머지 연산 
            #print (ilist2[1]) # 두번째로 큰수
            answer += int(ilist2[1])
        else: 
            #print (ilist2[0]) # 가장 큰수
            answer += int(ilist2[0])

    return answer

def example(i1, i2):
    answer = 0
    ilist1 = i1.split()  # n, m, k 차례 대로
    n = int(ilist1[0] ) # 배열의 크기
    m = int(ilist1[1] ) # 숫자가 더해지는 횟수
    k = int(ilist1[2] ) # k번 초과하여 더할 수 없음
    #print(ilist1)
    ilist2 = i2.split()
    #print(ilist2)
     # sort
    ilist2.sort()

    first = int(ilist2[n-1] )
    second = int(ilist2[n-2] )

    result = 0

    while True :
        for i in range(k):
            if m == 0 :
                break
            result += first
            m -= 1
        if m == 0 :
            break
        result  += second
        m -= 1

    return result


def example2(i1, i2):
    answer = 0
    ilist1 = i1.split()  # n, m, k 차례 대로
    n = int(ilist1[0] ) # 배열의 크기
    m = int(ilist1[1] ) # 숫자가 더해지는 횟수
    k = int(ilist1[2] ) # k번 초과하여 더할 수 없음

    ilist2 = i2.split()
     # sort
    ilist2.sort()

    first = int(ilist2[n-1] )
    second = int(ilist2[n-2] )

    # 가장 큰 수가 더해지는 횟수 계산
    count = int(m/(k+1)) *k
    # -> k+1 이 반복
    # m 을 (k+1) 로 나눈 몫이 수열이 반복되는 횟수
    # 다시 여기에 k를 곱해주면 가장 큰 수가 등장하는 횟수가 된다
    count += m % (k+1)

    result = 0
    result += (count) * first  # 가장 큰 수 더하기
    result += (m-count)  * second  # 두 번째 큰 수 더하기  

    return result

inp1 = "5 8 3"
inp2 = "2 4 5 4 6"

print("----- -----")
print(solution(inp1, inp2))
print("----- -----")
print(example(inp1, inp2))
print("----- -----")
print(example2(inp1, inp2))
