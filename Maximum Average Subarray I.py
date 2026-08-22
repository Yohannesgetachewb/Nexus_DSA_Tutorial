class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = s = sum(nums[:k])
        for i in range(k, len(nums)):
            curr += nums[i] - nums[i - k]
            if curr > s:
                s = curr
        return s / k
        
