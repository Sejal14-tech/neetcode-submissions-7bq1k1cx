class Solution:
    def findMin(self, nums: List[int]) -> int:
        #min on left and # max in mid
        if nums[0]<=nums[-1]:
            return nums[0]
        ans = float('inf')
        left = 0
        right = len(nums)-1
        while left<=right:
            mid = left + (right-left)//2
            if nums[mid]>nums[right]:
                left = mid+1
            else:
                ans = min(ans,nums[mid])
                right = mid-1
        return ans

































        # if nums[0]<nums[-1]:
        #     return nums[0]
        # ans = float('inf')
        # left = 0 
        # right = len(nums)-1
        # while left<=right:
        #     mid = left +(right-left)//2
        #     if nums[mid]>nums[right]:
        #         left = mid+1
        #     else:
        #         ans = min(ans,nums[mid])
        #         right = mid-1
        # return ans
        
        