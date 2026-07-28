class Solution:

    def encode(self, strs: List[str]) -> str:
        result = str()
        for string in strs:
            result += str(len(string)) + "#" + string
        return result
    def decode(self, s: str) -> List[str]:
        strs = list()
        while len(s) != 0:
            digits = s.index('#')
            length = int(s[0:digits])
            strs.append(s[digits+1:digits+1+length])
            s = s[digits+1+length:]
        return strs