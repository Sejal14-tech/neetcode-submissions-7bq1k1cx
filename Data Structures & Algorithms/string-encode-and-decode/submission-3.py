class Solution:

    def encode(self, strs: List[str]) -> str:
        strsm = ""
        for i in range(len(strs)):
            strsm+=str(len(strs[i]))+"#"+strs[i]
        return strsm

    def decode(self, s: str) -> List[str]:
        i = 0
        ans = []
        while i <len(s):
            j = i
            while s[j]!="#":
                j+=1
            length=int(s[i:j])
            word = s[j+1:length+j+1]
            ans.append(word)
            i=length+j+1
        return ans

