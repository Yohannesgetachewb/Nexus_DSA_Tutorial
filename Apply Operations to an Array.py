class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        write_idx = 0
        for i in range(n):
            if nums[i] != 0:
                nums[write_idx] = nums[i]
                write_idx += 1
        while write_idx < n:
            nums[write_idx] = 0
            write_idx += 1
            
        return nums
