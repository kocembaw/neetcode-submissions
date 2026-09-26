class Solution:
    def isValid(self, s: str) -> bool:
        seen = []
        pairs = {'}': '{', ']': '[', ')': '('}

        for nawias in s:
            if nawias not in paris:
                seen.append(nawias)
            else:
                if not seen or seen.pop() != pairs[nawias]:
                    return False
        return True