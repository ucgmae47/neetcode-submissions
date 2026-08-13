class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        longest = 1
        start, end = 0, 1
        letters = set(s[0])
        while end < len(s):
            if s[end] in letters:
                if end - start > longest:
                    longest = end - start
                while s[start] != s[end]:
                    letters.remove(s[start])
                    start += 1
                start += 1
                end += 1
            else:
                letters.add(s[end])
                end += 1
        print(end, start)
        if end - start > longest:
            longest = end - start
        return longest