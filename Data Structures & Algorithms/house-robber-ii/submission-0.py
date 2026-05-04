class Solution:
    def rob(self, nums: List[int]) -> int:
        def robbery(nums):
            dp =[0]*len(nums)
            dp[0]=nums[0]
            dp[1]=max(nums[0],nums[1])
            for i in range(2,len(nums)):
                dp[i]=max(dp[i-1],dp[i-2]+nums[i])
            return dp[-1]
        if len(nums)==1:
            return nums[0]
        elif len(nums)==2:
            return max(nums[0],nums[1])
        else:
            return max(robbery(nums[:-1]),robbery(nums[1:]))
        