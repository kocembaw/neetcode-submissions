from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ilosc_s = Counter(s)
        ilosc_t = Counter(t)
        
        for a in s:
            if ilosc_s[a] != ilosc_t[b]:
                return False
        return True
        
        
        