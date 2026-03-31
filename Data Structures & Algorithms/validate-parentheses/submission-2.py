class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dicts = {'}':'{',']':'[',')':'('}
        for i in range(len(s)):
            if s[i]=="(" or s[i]=="{" or s[i]=="[":
                stack.append(s[i])
            elif s[i] in dicts and len(stack)!=0:
                if stack.pop()!=dicts[s[i]]:
                    return False
            else:
                return False
        return len(stack)==0
        