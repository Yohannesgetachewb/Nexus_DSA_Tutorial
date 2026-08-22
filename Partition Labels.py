class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurrence = {char: idx for idx, char in enumerate(s)}
        
        result = []
        start = 0
        max_idx = 0
        for i, char in enumerate(s):
            max_idx = max(max_idx, last_occurrence[char])
            if i == max_idx:
                result.append(i - start + 1)
                start = i + 1
                
        return result
