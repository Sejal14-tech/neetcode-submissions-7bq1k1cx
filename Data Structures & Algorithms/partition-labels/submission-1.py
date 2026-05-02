class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        st = {}
        for i in range(len(s)):
            st[s[i]]=i
        res = []
        end = st[s[0]]
        start = 0
        print(st)
        for i in range(0,len(s)):
            if st[s[i]]>end:
                end = st[s[i]]
            if end==i:
                res.append(end-start+1)
                start = end+1
                end = 0
        return res

