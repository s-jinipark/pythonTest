
N = [1,2,3,4]
M = 2

# 순열
s =[]
def dfs():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    for i in N : #range(1, M+1):
        if i not in s :   # visited chk 격 인가  ?
            s.append(i)
            dfs()
            s.pop()
dfs()


print('--------------------')
# 조합
s = []
def dfs2(start):
    if len(s) == M :
        print(s)
        return
    for i in range(start, len(N)) :
        if N[i] not in s :
            s.append(N[i])
            dfs2(i+1)
            s.pop()
dfs2(0)


## extra
cat = 'cat'
dog = 'dog'
cow = 'cow'
ret = None

animal = 'dog'
if animal is dog:
    ret = dog
elif animal is cat:
    ret = cat
else:
    ret = cow
print("Default: " + ret)

#ret = dog if animal is dog else cat if animal is cat else cow
ret = 'D' if animal is dog else 'C' if animal is cat else cow
print("One-Line: " + ret)

#출처: https://info-lab.tistory.com/303 [:: IT School :::티스토리]
