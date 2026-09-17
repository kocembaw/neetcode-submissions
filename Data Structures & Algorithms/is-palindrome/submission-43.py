class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:

            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                 #wykona sie gdy znak nie jest literą ani cyfrą
                right -= 1

            #czy znaki pod left i right są takie same?
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True