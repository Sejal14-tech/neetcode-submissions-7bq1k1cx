from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # strs.sort(key=len(strs))
        dicts = {}
        for i in strs:
            m = "".join(sorted(i))
            if m not in dicts:
                dicts[m] = [i]
            else:
                dicts[m].append(i)
        ans = []
        for i in dicts.values():
            ans.append(i)
        return ans
            






















            # anagram_map = defaultdict(list)
            # for word in strs:
            #     count = [0]*26
            #     for i in word:
            #         count[ord(i)-ord('a')]+=1
            #     key =  tuple(count)
            #     anagram_map[key].append(word)
            # return list(anagram_map.values())

        