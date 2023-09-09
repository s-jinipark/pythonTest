
def solution(birthday):
    answer = []
    ''' 람다로 하면 될 거 같은데
    기억이 안 남 
    '''
    # s = '12/21'
    # print(s[:s.find('/')])
    # print(s[s.find('/')+1:])
    for i in range(len(birthday)):
        for j in range(i+1, len(birthday)):
            #print(i, j)
            si = birthday[i][:birthday[i].find('/')]
            sj = birthday[j][:birthday[j].find('/')]
            print(si, sj)
            tmp = ''
            if si >  sj :
                tmp = birthday[i]
                birthday[i] = birthday[j]
                birthday[j] = tmp
        print(birthday)
    return answer


birthday = ["9/27", "10/13", "5/9", "9/4"]

an = solution(birthday)
print(an)