class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        i = 0
        while i < len(temperatures):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                index = stack.pop()
                res[index]=i-index
            stack.append(i)
            i+=1
        return res
        