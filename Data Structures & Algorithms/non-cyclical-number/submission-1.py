class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            sums = 0
            while n > 0:
                sums+=(n%10)**2
                n=n//10
            return sums
        seen = set()
        while n!=1 and n not in seen:
            seen.add(n)
            n  = get_next(n)
        return n==1


        