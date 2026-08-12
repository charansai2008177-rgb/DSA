from collections import Counter
#example
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1 = Counter(s)
        freq2 = Counter(t)
        if freq1==freq2:
            return True
        return False
        
        