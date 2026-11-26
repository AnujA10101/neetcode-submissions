class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out_p = [1] * len(nums)
        prefix = 1

        for i in range(len(nums)):
            out_p[i] = prefix
            prefix *= nums[i]
        
        out_s = [1] * len(nums)
        suffix = 1

        for i in range(len(nums)- 1, -1, -1):
            out_s[i] = suffix 
            suffix *= nums[i]
        
        res = [1] * len(nums)
    
        for i in range(len(nums)):
            res[i] = (out_p[i] * out_s[i])
        
        return res



