class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency = [0] * 26
        frequency[ord(s[0])-ord('A')] = 1
        left = 0
        right = 1
        maximum = 1
        while True:
            while right - left - max(frequency) <= k:
                if right >= len(s):
                    return max(maximum, right - left)
                frequency[ord(s[right])-ord('A')] += 1
                right += 1
            maximum = max(maximum, right - left - 1)
            while right - left - max(frequency) > k:
                frequency[ord(s[left])-ord('A')] -= 1
                left += 1