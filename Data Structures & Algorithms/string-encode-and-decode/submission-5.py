class Solution:
    def encode(self, strs: List[str]) -> str:
        encode_strsm=''
        for i in range(len(strs)):
            encode_strsm += str(len(strs[i])) + "*" + strs[i]
        return encode_strsm
    def decode(self, s: str) -> List[str]:
        i = 0
        j = 0
        res =[]
        print(s)
        while i<len(s):
            while s[i]!='*':
                i+=1
            length = int(s[j:i])
            print(length,s[i+1:i+length+1])
            res.append(s[i+1:i+length+1])
            j=i+length+1
            i=i+length+1
        return res










    # def encode(self, strs: List[str]) -> str:
    #     strsm = ""
    #     for i in range(len(strs)):
    #         strsm+=str(len(strs[i]))+"#"+strs[i]
    #     return strsm

    # def decode(self, s: str) -> List[str]:
    #     i = 0
        # ans = []
        # while i <len(s):
        #     j = i
        #     while s[j]!="#":
        #         j+=1
        #     length=int(s[i:j])
        #     word = s[j+1:length+j+1]
        #     ans.append(word)
        #     i=length+j+1
        # return ans

