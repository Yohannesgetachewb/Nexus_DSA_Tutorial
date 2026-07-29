class Solution:
    def similarPairs(self, words: List[str]) -> int:
        freq = {}
        ans = 0

        for word in words:
            mask = 0
            for char in word:
                mask |= 1 << (ord(char)- ord('a'))

            ans += freq.get(mask , 0)
            freq[mask] = freq.get(mask , 0) + 1
        return ans
