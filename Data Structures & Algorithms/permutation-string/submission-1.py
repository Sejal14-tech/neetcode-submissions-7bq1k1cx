class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        store = {}
        if len(s1)>len(s2):
            return False
        for i in s1:
            store[i] = store.get(i,0)+1
        check = {}
        start = 0
        for i in range(len(s2)):
            check[s2[i]]=check.get(s2[i],0)+1
            if i-start+1>len(s1):
                check[s2[start]]-=1
                if check[s2[start]]==0:
                    del check[s2[start]]
                start+=1
            if check==store:
                return True
        return False

        