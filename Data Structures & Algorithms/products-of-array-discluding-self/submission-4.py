class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
        prod = nums[0]
        for i in range(1,len(nums)):
            prefix[i]=prod
            prod*=nums[i]
        suffix = 1
        print(prefix)
        for i in range(len(nums)-1,-1,-1):
            prefix[i]=suffix*prefix[i]
            suffix*=nums[i]
        return prefix



















        # #product at i without i  = product before i*product after i
        # res = [0]*len(nums)
        # prefix=1
        # for i in range(len(nums)):
        #     res[i]=prefix
        #     prefix*=nums[i]
        # suffix = 1
        # for i in range(len(nums)-1,-1,-1):
        #     res[i]=suffix*res[i]
        #     suffix*=nums[i]
        # return res


        