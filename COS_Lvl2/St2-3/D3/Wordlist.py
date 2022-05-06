def solution(sample):
    #answer = None
    answer = []
    # 코드를 작성하세요.

    dic_sam = {}
    for s in sample :
        print(s.lower())
        tmp = s.lower()
        if tmp in dic_sam :
            dic_sam[tmp] +=1
        else :
            dic_sam[tmp] =1
    print(dic_sam)

    #dic_sam = sorted(dic_sam.items())
    #dic_sam = sorted(dic_sam.items(), key = lambda item: item[1], reverse=True)
    #print(dic_sam)

    tmplist = [(c, dic_sam[c]) for c in dic_sam]
    #tmplist.sort(key=lambda x : x[1])  # 오름차순
    #tmplist.sort(key=lambda x: -x[1])  # 내림차순
    tmplist.sort(key=lambda x: (-x[1], x[0]) )  # 내림차순

    print(tmplist)
    answer = [c[0] for c in tmplist]

    return answer


sample = ["propose", "change", "teach", "propose", "teach", "program", "Change", "make","teach"]
res = solution(sample)
print(res)












