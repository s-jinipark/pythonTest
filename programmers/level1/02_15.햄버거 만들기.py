
# 빵 – 야채 – 고기 - 빵
# 1, 2, 3 중 하나의 값이며, 순서대로 빵, 야채, 고기를 의미
# [즉, 1-2-3-1 의 순서]
def solution(ingredient):
    answer = 0
    s = []
    for i in ingredient :
        s.append(i)
        print(s, s[-4:])
        if s[-4:] == [1,2,3,1] :
            answer += 1
            for _ in range(4):
                s.pop()
                # 만약 s = s[:-4] # 해당 부분으로 인해 시간 초과 발생
    return answer

ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]

re = solution(ingredient)
print(re)

'''
[기존] 통과 못함

def solution(ingredient):
    answer = 0
    연습 = ''
    for i in ingredient :
        연습 += str(i)
    while True :
        t_num = 연습.find('1231')
        if t_num > 0:
            #print(연습.find('1231') , 연습[:t_num] , 연습[t_num:t_num+4] , 연습[t_num+4:])
            연습 = 연습[:t_num] + 연습[t_num+4:]
            answer += 1
        else :
            break

    #print(연습)

    return answer
    
'''