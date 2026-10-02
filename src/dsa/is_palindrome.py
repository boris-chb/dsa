class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                print("Not Palindrome! :(")
                return False
            left += 1
            right -= 1
        print("Palindrome!")
        return True


if __name__ == "__main__":
    s = Solution()
    s.isPalindrome("Abba")
    s.isPalindrome("Aa")
    s.isPalindrome("Was it a car or a cat I saw?")
    s.isPalindrome("Wazzzzup??")
