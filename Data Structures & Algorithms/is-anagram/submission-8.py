from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ilosc_s = Counter(s)
        ilosc_t = Counter(t)
        
        if ilosc_s == ilosc_t:
            return True
        return False
        
        
        