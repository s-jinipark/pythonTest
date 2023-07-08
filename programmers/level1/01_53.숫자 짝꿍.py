def solution(X, Y):
    answer = ''
    tmp = []
    xlist = list(X)
    ylist = list(Y)
    xlist.sort()
    ylist.sort()
    print(xlist, ylist)
    # 시간 초과 나서 ..


    # for i in range(len(xlist)) :
    #     for j in range(len(ylist)) :
    #         if xlist[i] == ylist[j] :
    #             print('>', ylist[j])
    #             #ylist.pop(j)  # 오류남
    #             연습.append(ylist[j])
    #             ylist[j] = '-1'
    #             break
    # if len(연습) == 0 :
    #     return "-1"
    # #print(xlist)
    # 연습.sort(reverse=True)
    # print(연습)
    # if len(연습) > 1 and 연습[0] =='0':
    #     return '0'
    # for t in 연습:
    #     answer += t

    return answer

# X = "100"
# Y = "2345"
# X = "100"
# Y = "123450"
X = "100"
Y = "203045"

re = solution(X, Y)
print(re)

print("====================")

