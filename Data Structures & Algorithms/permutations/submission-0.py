class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = [False]*len(nums)
        def backtrack(res,curr):
            if len(curr)==len(nums):
                res.append(curr[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i]=True
                curr.append(nums[i])
                backtrack(res,curr)
                curr.pop()
                used[i]=False
        res = []
        curr = []
        backtrack(res,curr)
        return res
        