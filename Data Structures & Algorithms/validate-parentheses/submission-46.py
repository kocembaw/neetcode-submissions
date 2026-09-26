class Solution:
    def isValid(self, s: str) -> bool:
        seen = []
        pairs = {']': '[', '}': '{', ')': '('}
        for nawias in s:
            if nawias not in pairs:
                seen.append(nawias)
            if seen and seen.pop() != pairs[nawias]:
                return False
            
        return True
