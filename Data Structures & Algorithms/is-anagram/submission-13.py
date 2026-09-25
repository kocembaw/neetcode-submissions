class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_s = {}
        seen_t = {}
        for chs, cht in zip(s,t):
            seen_s[chs] = seen_s.get(chs, 0) + 1
            seen_t[cht] = seet_t.get(cht, 0) + 1
        return seen_s == seen_t