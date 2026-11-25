class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        out = []

        for s in strs:
            seen["".join(sorted(s))].append(s)
        
        for val in seen.values():
            out.append(val)
        
        return out
            
        