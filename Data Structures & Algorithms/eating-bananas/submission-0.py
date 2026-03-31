class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        # [1,2....25]
        1 +12
        ans =1
        def feasible(rate):
            hours = 0
            for i in piles:
                hours +=(i+rate-1)//rate
            return hours
        while left<=right:
            mid = left + (right-left)//2
            if feasible(mid)>h:
                left= mid+1
            else:
                ans = mid
                right = mid-1
        return ans

        