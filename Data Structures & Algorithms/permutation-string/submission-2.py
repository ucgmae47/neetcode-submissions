class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        counts_s1 = {}
        counts_s2 = {}
        for letter in s1:
            counts_s1[letter] = counts_s1.get(letter, 0) + 1
        for letter in s2[0:len(s1)]:
            counts_s2[letter] = counts_s2.get(letter, 0) + 1
        if counts_s1 == counts_s2:
                return True
        for index in range(1, len(s2) - len(s1) + 1):
            counts_s2[s2[index-1]] -= 1
            if counts_s2[s2[index-1]] == 0:
                counts_s2.pop(s2[index-1])
            counts_s2[s2[index+len(s1)-1]] = counts_s2.get(s2[index+len(s1)-1], 0) + 1
            if counts_s1 == counts_s2:
                return True
        return False