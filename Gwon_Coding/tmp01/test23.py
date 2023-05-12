
# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다.
# 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만,
# aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
#
# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

# => 앞에 나왔던 알파벳을 저장하고, 바로 직전 알파벳을 저장하여 체크한다


#N = int(input())
#N = 3
N = 4

# test = []
# for _ in range(N):
#     test.append(input())

#test = ['happy', 'new', 'year']
test = ['aba', 'abab', 'abcabc', 'a']


cnt = 0

for t in test:
    hist = [t[0]]   # 나왔던 알파벳 기록
    prev = t[0]   # 이전 알파벳
    print(t)
    for i in range(1, len(t)):
        print(t[i])
        if t[i] != t[i-1] and t[i]  in hist :
            break
        else :
            hist.append(t[i])
    else :
        cnt += 1

print(cnt)