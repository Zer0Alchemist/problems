class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        
        for n in range(k, len(s2) + 1):
            if sorted(s1) == sorted(s2[n - k: n]):
                return True
        
        return False