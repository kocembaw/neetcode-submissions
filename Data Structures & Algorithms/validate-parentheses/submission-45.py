class Solution:
    def isValid(self, s: str) -> bool:
        seen = []
        pairs = {']': '[', '}': '{', ')': '('}
        for nawias in s:
            if seen and seen.pop() != pairs[nawias]:
                return False
            if nawias not in pairs:
                seen.append(nawias)
        return True
