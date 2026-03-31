class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicts = {}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s[i] not in dicts:
                dicts[s[i]]=1
            else:
                dicts[s[i]]+=1
        for i in range(len(t)):
            if t[i] in dicts:
                dicts[t[i]]-=1
            else:
                return False
            if dicts[t[i]]==0:
                dicts.pop(t[i])
        return True
    




        