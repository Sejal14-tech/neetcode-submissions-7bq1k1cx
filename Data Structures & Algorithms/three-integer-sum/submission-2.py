class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        for i in range(len(nums)-2):
            target =-nums[i]
            left = i+1
            right = len(nums)-1
            while left<right:
                if nums[left]+nums[right]==target:
                    ans.add((nums[i],nums[left],nums[right]))
                    left+=1
                    right-=1
                elif nums[left]+nums[right]>target:
                    right-=1
                else:
                    left+=1
        final = [i for i in ans]
        return final
        