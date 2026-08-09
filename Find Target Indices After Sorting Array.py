class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        less_than = 0
        count = 0
        
        for num in nums:
            if num < target:
                less_than += 1
            elif num == target:
                count += 1
                
        return list(range(less_than, less_than + count))
