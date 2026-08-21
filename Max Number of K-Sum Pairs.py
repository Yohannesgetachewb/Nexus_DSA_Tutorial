from collections import defaultdict
from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        operations = 0
        
        for num in nums:
            target = k - num
            if count[target] > 0:
                operations += 1
                count[target] -= 1
            else:
                count[num] += 1
                
        return operations
        
