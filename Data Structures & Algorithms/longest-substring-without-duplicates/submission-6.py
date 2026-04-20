class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dicts={}
        j =0
        length=0
        for i in range(len(s)):
            if s[i] in dicts:
                j = max(dicts[s[i]]+1,j)
            length = max(length,i-j+1)
            dicts[s[i]]=i
        return length





































        # if len(s)==0:
        #     return 0
        # store = {}
        # start = 0
        # end = 0
        # max_length=1
        # for end in range(len(s)):
        #     if s[end] in store:
        #         start = max(start,store[s[end]]+1)
        #     length = end-start+1
        #     max_length = max(length,max_length)
        #     store[s[end]]=end
        # return max_length

