class Solution:
    def isValid(self, s: str) -> bool:
        seen = []
        pairs = {'}': '{', ')': '(', ']': '['}

        for nawias in s:
            if nawias in pairs and seen:
                if seen.pop() != pairs[nawias]:
                    return False
            else:
                seen.append(nawias)
            
         
        return not seen