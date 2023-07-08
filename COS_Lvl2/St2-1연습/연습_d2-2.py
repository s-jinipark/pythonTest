# 대소문자 구분하지 않고 단어의 빈도를 기준으로 내림차순 정렬합니다. (소문자로 맞춥니다.)
# 사용 빈도가 같은 단어가 여러개 있다면 알파벳 순으로 내림차순(또는 오름차순) 정렬합니다.
# 라이브러리를 이용하지 않고 버블정렬 알고리즘을 이용하는 경우
# ['teach', 'propose', 'change', 'program', 'make']

sample = ["propose", "change", "teach", "propose", "teach", "program", "Change", "make", "teach"]
answer = []
tmp = {}
# for w in sample:
#     w1 = w.lower()
#     if w1 in 연습:
#         연습[w1] += 1
#     else:
#         연습[w1] = 1

# [2번째 연습] 딕셔너리에 넣는 거 , dict 는 {} 라는 점
for w in sample :
    w1 = w.lower()
    if w1  in tmp :
        tmp[w1] += 1
    else :
        tmp[w1] = 1

print(tmp)

#tmplist = [[c, 연습[c]] for c in 연습]
# 이거슨 리스트의 리스트 군
# ***** 이부분 중요
tmplist = [[c, tmp[c]] for c in tmp]
print(tmplist)
    # 이 것도 되긴하지만 ->
    # tmplist2 = [(c, 연습[c]) for c in 연습]
    # print(tmplist2)
    # 아래에서 문제 발생
    #TypeError: 'tuple' object does not support item assignment

# for i in range(len(tmplist)):
#     for j in range(len(tmplist)-1-i):
#         if tmplist[j][1] < tmplist[j+1][1]:
#             연습 = tmplist[j]
#             tmplist[j] = tmplist[j+1]
#             tmplist[j+1] = 연습
#         elif tmplist[j][1] == tmplist[j+1][1]:
#             if tmplist[j][0] > tmplist[j+1][0]:
#                 연습 = tmplist[j]
#                 tmplist[j] = tmplist[j + 1]
#                 tmplist[j + 1] = 연습

# [2] 2단계 버블 정렬
# 답은 ['teach', 'change', 'propose', 'make', 'program']
for i in range(len(tmplist)) :
    for j in range(len(tmplist) -1 ) :
        # 버블로 , i는 횟수 채운다고 보면 됨
        if tmplist[j][1] < tmplist[j+1][1] : # 많은게 앞이니까
            temp = []
            temp = tmplist[j]  #temp = tmplist[j][1]  # 오답
            tmplist[j]  = tmplist[j+1]  #tmplist[j][1] = tmplist[j][1]
            tmplist[j+1] = temp
        elif  tmplist[j][1] == tmplist[j+1][1] :
            if tmplist[j][0] > tmplist[j + 1][0]:  # 많은게 앞이니까
                temp = []
                temp = tmplist[j]  # temp = tmplist[j][1]  # 오답
                tmplist[j] = tmplist[j + 1]  # tmplist[j][1] = tmplist[j][1]
                tmplist[j + 1] = temp

    print(tmplist)

print(tmplist)

for w in tmplist:
    answer.append(w[0])

print(answer)


