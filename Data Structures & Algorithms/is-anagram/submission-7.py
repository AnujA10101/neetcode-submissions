from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seen = defaultdict(int)

        for char in s:
            seen[char] += 1

        for char in t:
            seen[char] -= 1
        
        for val in seen.values():
            if val != 0:
                return False
        
        return True 
        