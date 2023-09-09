def isPalindrome(string):
    left = 0
    right = len(string) - 1
    print('>', string)
    #while left != right:
    while left <= right:
        print(string[left] ,  string[right])
        if string[left] != string[right]:
            return False

        left += 1
        right -= 1

    return True

def solution(palindrome):
    count = 0

    for string in palindrome:
        if isPalindrome(string):
            count += 1

    return count



palindrome = ["aBa", "bccb", "AbBa"]

an = solution(palindrome)
print(an)