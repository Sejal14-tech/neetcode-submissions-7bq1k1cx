class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def backtrack(index,curr):
            if index == len(nums):
                res.add(tuple(sorted(curr)))
                return
            backtrack(index+1,curr)
            curr.append(nums[index])
            backtrack(index+1,curr)
            curr.pop()
        curr = []
        backtrack(0,curr)
        return [i for i in res]