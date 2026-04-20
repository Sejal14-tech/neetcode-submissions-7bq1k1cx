
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs.sort(key = lambda x : len(x))
        dicts={}
        for i in range(len(strs)):
            temp = "".join(sorted(strs[i]))
            if temp not in dicts:
                dicts[temp] = [strs[i]]
            else:
                dicts[temp].append(strs[i])
        return [value for key,value in dicts.items()]























            # anagram_map = defaultdict(list)
            # for word in strs:
            #     count = [0]*26
            #     for i in word:
            #         count[ord(i)-ord('a')]+=1
            #     key =  tuple(count)
            #     anagram_map[key].append(word)
            # return list(anagram_map.values())

        