class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return False

        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r += 1
            if s[l] != s[r]:
                return False
        return True