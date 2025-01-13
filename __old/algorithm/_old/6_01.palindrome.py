
# 팰린드롬
# 주어진 문자열이 팰린드롬인지 확인하라.
# 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.
# A man, a plan, a canal: Panama => true
# race a car => false

import collections
from typing import Collection, Deque


str = "A man, a plan, a canal: Panama"
# 공백제거
str = str.replace(" ", "")

#print(str[0:5])
temp = []

for i in range(len(str)) :
    #print(str[i])
    #if str[i].isalpha or str[i].isnumeric :
    if str[i].isalnum :
        temp.append(str[i].lower())
print(temp)


# [2]
# str2 = "A man, a plan, a canal: Panama"
str2 = "race a car"
temp2 = []

for char in str2 :
    #print(char)
    if char.isalnum() :
        temp2.append(char.lower())
print(temp2)
# -> str 을 잘랐을 경우는 , 가 포함되나
# char 로 했을 경우는 , 가 제외 됨

is_palin = True
# print(int(len(temp2)/2) )
cnt = len(temp2)
rev_num = cnt-1 # reverse_num
for i in range(cnt) :
    #print(i)
    if temp2[i] != temp2[rev_num]:
        print(temp2[i] + "/" + temp2[rev_num]) 
        is_palin = False
        break
    rev_num = rev_num -1
print(is_palin)


#####
class Solution:
    # 풀이 1
    # 리스트로 변환
    def isPalindrome1( self, s:str) -> bool:
        strs = []
        for char in s:
            if char.isalnum() :
                strs.append(char.lower())

        while len(strs) > 1 :
            if strs.pop(0) != strs.pop() : # 0 을 지정하면 맨앞의 값, pop() 은 맨 뒷부분
                return False

        return True

    # 풀이 2
    # 데크 자료형을 이용한 최적화
    def isPalindrome2( self, s:str) -> bool:
        # 자료형 데크로 선언
        strs : Deque = collections.deque()

        for char in s:
            if char.isalnum() :
                strs.append(char.lower())
        
        while len(strs) > 1 :
            if strs.popleft() != strs.pop():
                return False
        return True

# def main():
sol = Solution()
s = "A man, a plan, a canal: Panama"
print(sol.isPalindrome1(s))

print(sol.isPalindrome2(s))

# if __name__ == "__main__":
#     main()
