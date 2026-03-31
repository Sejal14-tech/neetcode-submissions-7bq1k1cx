class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicts= {}
        for i in range(len(nums)):
            if target-nums[i] in dicts:
                return [dicts[target-nums[i]],i]
            dicts[nums[i]]=i

        