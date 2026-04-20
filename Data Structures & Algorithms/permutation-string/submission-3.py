class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        store = {}
        for i in range(len(s1)):
            store[s1[i]]=store.get(s1[i],0)+1
        store2 = {}
        j = 0
        i=0
        while i <len(s2):
            store2[s2[i]]=store2.get(s2[i],0)+1
            print(store2)
            if i-j+1==len(s1):
                if store2==store:
                    return True
                else:
                    store2[s2[j]]-=1
                    if store2[s2[j]]==0:
                        del store2[s2[j]]
                    j+=1
            i+=1
        return store2==store


        
                


















        # store = {}
        # if len(s1)>len(s2):
        #     return False
        # for i in s1:
        #     store[i] = store.get(i,0)+1
        # check = {}
        # start = 0
        # for i in range(len(s2)):
        #     check[s2[i]]=check.get(s2[i],0)+1
        #     if i-start+1>len(s1):
        #         check[s2[start]]-=1
        #         if check[s2[start]]==0:
        #             del check[s2[start]]
        #         start+=1
        #     if check==store:
        #         return True
        # return False

        