class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        min_freq = [float('inf')] * 26
        
        for word in words:
            char_freq = [0] * 26
            for ch in word:
                char_freq[ord(ch) - ord('a')] += 1
            for i in range(26):
                min_freq[i] = min(min_freq[i], char_freq[i])
        result = []
        for i in range(26):
            if min_freq[i] > 0:
                result.extend([chr(ord('a') + i)] * min_freq[i])
                
        return result
        
