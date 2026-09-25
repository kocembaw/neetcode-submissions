class Solution:
    def isValid(self, s: str) -> bool:
        seen = []
        pairs = {']': '[', '}': '{', ')': '('}
        for nawias in s:
            if nawias in pairs:
                if seen and seen.pop() != nawias:
                    return False
            seen.append(nawias)
        return True
