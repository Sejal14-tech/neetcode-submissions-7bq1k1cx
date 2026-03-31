class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        store = {}
        start = 0
        end = 0
        max_length=1
        for end in range(len(s)):
            if s[end] in store:
                length = end-start
                max_length = max(length,max_length)
                start = max(start,store[s[end]]+1)
            else:
                length = end-start+1
                max_length = max(length,max_length)
            store[s[end]]=end
        return max_length

