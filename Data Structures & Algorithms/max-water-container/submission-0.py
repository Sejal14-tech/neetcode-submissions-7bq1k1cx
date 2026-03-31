class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        left = 0
        right = len(heights)-1
        while left<right:
            if heights[right]>=heights[left]:
                water = heights[left]*(right-left)
                left+=1
            else:
                water = heights[right]*(right-left)
                right-=1
            max_water = max(water,max_water)
        return max_water
            

            

        