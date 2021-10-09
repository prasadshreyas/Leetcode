class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # Kadane's algorithm
        maxS = nums[0]
        curS = maxS
        for i in range(1,len(nums)):
            curS = max(nums[i], curS+nums[i])
            maxS = max(maxS, curS)
            
        return maxS
