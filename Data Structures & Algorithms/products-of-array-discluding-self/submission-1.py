class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prd = 1
        zero = 0
        for i in nums:
            if i!=0:
                prd*=i
            else:
                zero+=1
        for i in range(len(nums)):
            if nums[i]!=0 and zero==0:
                nums[i] = prd//nums[i]
            elif nums[i]==0 and zero>1:
                nums[i]=0
            elif nums[i]==0 and zero==1:
                nums[i]=prd
            else:
                nums[i]=0

        return nums
        

        