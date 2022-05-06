# 대소문자 구분하지 않고 단어의 빈도를 기준으로 내림차순 정렬합니다. (소문자로 맞춥니다.)
# 사용 빈도가 같은 단어가 여러개 있다면 알파벳 순으로 내림차순(또는 오름차순) 정렬합니다.
# 라이브러리를 이용하지 않고 버블정렬 알고리즘을 이용하는 경우
# ['teach', 'propose', 'change', 'program', 'make']

sample = ["propose", "change", "teach", "propose", "teach", "program", "Change", "make", "teach"]
answer = []
tmp = {}
for w in sample:
    w1 = w.lower()
    if w1 in tmp:
        tmp[w1] += 1
    else:
        tmp[w1] = 1

print(tmp)

tmplist = [[c, tmp[c]] for c in tmp]

print(tmplist)

for i in range(len(tmplist)):
    for j in range(len(tmplist)-1-i):
        if tmplist[j][1] < tmplist[j+1][1]:
            tmp = tmplist[j]
            tmplist[j] = tmplist[j+1]
            tmplist[j+1] = tmp
        elif tmplist[j][1] == tmplist[j+1][1]:
            if tmplist[j][0] > tmplist[j+1][0]:
                tmp = tmplist[j]
                tmplist[j] = tmplist[j + 1]
                tmplist[j + 1] = tmp

print(tmplist)

for w in tmplist:
    answer.append(w[0])

print(answer)
















