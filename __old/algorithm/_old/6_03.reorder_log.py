

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
logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]

sol.reverse_string(logs)

# if __name__ == "__main__":
#     main()
