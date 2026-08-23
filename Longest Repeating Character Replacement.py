class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pos = {}
        left = max_len = 0
        for right, char in enumerate(s):
            if char in pos and pos[char] >= left:
                left = pos[char] + 1
            pos[char] = right
            if right - left + 1 > max_len:
                max_len = right - left + 1
        return max_len
        
