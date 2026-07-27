class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = list(enumerate(strs))
        length = len(words)
        i = 0
        while i < length:
            words[i] = (words[i][0], sorted(words[i][1]))
            i += 1
        words.sort(key=lambda x:x[1])
        temp = words[0][1]
        chain = list()
        res = list()
        for i in range(length):
            if words[i][1] == temp:
                chain += [strs[words[i][0]]]
            else:
                res.append(chain)
                chain = list()
                temp = words[i][1]
                chain += [strs[words[i][0]]]
        res.append(chain)
        return res

