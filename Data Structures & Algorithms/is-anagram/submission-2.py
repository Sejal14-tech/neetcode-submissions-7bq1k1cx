class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        store = {}
        for i in range(len(s)):
            store[s[i]]=store.get(s[i],0)+1
        for i in range(len(t)):
            if t[i] in store:
                store[t[i]]-=1
                if store[t[i]]==0:
                    del store[t[i]]
            else:
                return False
        return len(store)==0
                





















        # dicts = {}
        # if len(s)!=len(t):
        #     return False
        # for i in range(len(s)):
        #     if s[i] not in dicts:
        #         dicts[s[i]]=1
        #     else:
        #         dicts[s[i]]+=1
        # for i in range(len(t)):
        #     if t[i] in dicts:
        #         dicts[t[i]]-=1
        #     else:
        #         return False
        #     if dicts[t[i]]==0:
        #         dicts.pop(t[i])
        # return len(dicts)==0
    




        