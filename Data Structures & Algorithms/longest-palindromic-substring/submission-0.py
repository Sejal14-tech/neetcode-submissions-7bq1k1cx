class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = float('-inf')
        res = []
        def expand(left,right):
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
            return left,right,right-left+1
        for i in range(len(s)):
            l1,r1,len1 = expand(i,i)
            l2,r2,len2 = expand(i,i+1)
            if len1>ans:
                ans = len1
                res = [l1+1,r1]
            if len2>ans:
                ans = len2
                res=[l2+1,r2]
        return s[res[0]:res[1]]