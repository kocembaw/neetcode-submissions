class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen_s = {}
        seen_t = {}
        for a, b in zip(s, t):
            seen_s[a] = seen_s.get(a, 0) + 1
            seen_t[b] = seen_t.get(b, 0) + 1
        return seen_s == seen_t