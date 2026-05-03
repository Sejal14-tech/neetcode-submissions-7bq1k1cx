class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(nums,curr,index,res):
            if index==len(nums):
                res.append(curr.copy())
                return
            curr.append(nums[index])
            backtrack(nums,curr,index+1,res)
            curr.pop()
            backtrack(nums,curr,index+1,res)
        curr = []
        res = []
        index = 0
        backtrack(nums,curr,index,res)
        return res


        