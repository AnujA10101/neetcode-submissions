class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for i in nums:
            res[i] = res.get(i, 0) + 1
        sort_val = sorted(list(res.items()), key=lambda x: x[1], reverse=True)
        sol = []
        for i in range(k):
            sol.append(sort_val[i][0])
            
        return sol
        
        