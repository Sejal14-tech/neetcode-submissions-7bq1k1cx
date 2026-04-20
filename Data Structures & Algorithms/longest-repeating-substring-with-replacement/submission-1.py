class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dicts = {}
        max_freq=0
        j=0
        length=1
        for i in range(len(s)):
            dicts[s[i]] = dicts.get(s[i],0)+1
            max_freq = max(max_freq,dicts[s[i]])
            if (i-j+1)-max_freq>k:
                dicts[s[j]]-=1
                j+=1
            length = max(length,i-j+1)
        return length




















        # start = 0
        # end = 0
        # max_freq = 0
        # max_length = 0
        # count={}
        # for end in range(len(s)):
        #     count[s[end]] = count.get(s[end], 0) + 1
        #     max_freq = max(max_freq,count[s[end]])
        #     if end-start+1-max_freq>k:
        #         count[s[start]]-=1
        #         start+=1
        #     max_length = max(end-start+1,max_length)
        # return max_length