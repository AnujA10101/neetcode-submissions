class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            seen[num] = 1 + seen.get(num, 0)
        
      
        for num, val in seen.items():
            freq[val].append(num)
        
        res = []

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        
        