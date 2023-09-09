

# 해설 보고 품
# 어렵게 생각해서 .ㅠ.ㅠ
def solution(birthday):
    answer = []
    bd = []
    for b in birthday:
        month, day = map(int, b.split('/'))   # <= **
        s1 = b[:b.find('/')]
        s2 = b[b.find('/')+1:]
        print('>', s1, s2)
        print(month, day)
        bd.append([month, day])
    bd.sort()
    print(bd)
    # 같은 달 중 에서도 일 별로 sort 해야 할 거 같은데 . . .
    for b in bd:
        answer.append(str(b[0]) + '/' + str(b[1]))

    return answer


#birthday = ["9/27", "10/13", "5/9", "9/4"]
# 내가 추가한 test
birthday = ["9/27", "9/3", "10/13", "5/9", "9/4"]
# 우와 sort 가 일 단위 까지 됨.

an = solution(birthday)
print(an)