class Solution:

    def encode(self, strs: List[str]) -> str:
        result = str()
        strs = [(str(len(string)) + '#' + string) for string in strs]
        return ''.join(strs)
    def decode(self, s: str) -> List[str]:
        result = list()
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            digits = j - i
            length = int(s[i:j])
            result.append(s[j+1:j+1+length])
            i = j + length + 1
        return result
