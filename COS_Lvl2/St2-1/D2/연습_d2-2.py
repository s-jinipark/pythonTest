
def solution1(tmp) :
    dic = {}   # 딕셔너리에 적재
    for w0 in tmp :
        w = w0.lower()
        if w in dic :
            dic[w] += 1
        else :
            dic[w] = 1
    print(dic)

    # 리스트 로 변환 *
    tmplist = [[c, dic[c]] for c in dic]
    print(tmplist)

    # 버블소트 *
    for i in range(len(tmplist)) :
        for j in range(len(tmplist)-1) :
            # 개수 비교
            if tmplist[j][1] < tmplist[j+1][1] :
                ttmp = tmplist[j+1]
                tmplist[j+1] = tmplist[j]
                tmplist[j] = ttmp
            elif tmplist[j][1] == tmplist[j+1][1] :
                if tmplist[j][0] > tmplist[j + 1][0]:  # 같을 땐 0 의 값 비교
                    ttmp = tmplist[j + 1]
                    tmplist[j + 1] = tmplist[j]
                    tmplist[j] = ttmp

        print(tmplist)
    rtn = []
    for i in tmplist :
        rtn.append( i[0] )
    print(rtn)

def main() :
    print('정렬')
    sample = ["propose", "change", "teach", "propose", "teach", "program", "Change", "make", "teach"]
    print(sample)
    print()
    solution1(sample)
    #['teach', 'change', 'propose', 'make', 'program']

if __name__ == '__main__' :
    main()