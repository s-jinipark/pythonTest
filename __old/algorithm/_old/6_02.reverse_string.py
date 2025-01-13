
# 문자열 뒤집기
# 입력값은 문자 배열이며, 리턴 없이 리스트 내부를 직접 조작하라


from typing import List


class Solution:

    def reverse_string( self, s:List[str]) -> None:

        for char in s:
            print(char)
        left, right = 0 , len(s)-1
        while left < right :
            s[left], s[right] = s[right], s[left]
            left += 1
            right -=1

# def main():
sol = Solution()
lst = ["h", "e", "l", "l", "o"]

sol.reverse_string(lst)
print(lst)

# if __name__ == "__main__":
#     main()
