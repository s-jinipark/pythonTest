# 대소문자 구분하지 않고 단어의 빈도를 기준으로 내림차순 정렬합니다. (소문자로 맞춥니다.)
# 사용 빈도가 같은 단어가 여러개 있다면 알파벳 순으로 내림차순(또는 오름차순) 정렬합니다.
# 라이브러리 함수와 lambda 식 이용하는 경우
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

tmplist = [[c, tmp[c]] for c in tmp]
print(tmplist)
tmplist.sort(key=lambda x : (x[1], x[0]), reverse = True)    # 두 조건 모두 내림차순
print(tmplist)

sortres = sorted(sorted(tmplist, key=lambda x: x[0]), key=lambda x: -x[1])
print(sortres)

for w in sortres:
    answer.append(w[0])

print(answer)
















