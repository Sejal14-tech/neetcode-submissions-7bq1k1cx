class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        def backtrack(nums,target,res,curr,store,index):
            if curr==target:
                res.append(store.copy())
                return
            if curr > target:
                return
            for i in range(index,len(nums)):
                store.append(nums[i])
                backtrack(nums,target,res,curr+nums[i],store,i)
                store.pop()
        res = []
        curr=0
        store=[]
        index= 0 
        backtrack(nums,target,res,curr,store,index)
        return res

        