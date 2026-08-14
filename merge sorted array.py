class Solution:
    """
        Do not return anything, modify nums1 in-place instead.
        """

    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int ) -> None:
   
        nums1_copy = nums1[:m]

        p1 = 0  
        p2 = 0  
        for p in range(m + n):
         if p2 >= n or (p1 < m and nums1_copy[p1] <= nums2[p2]):
            nums1[p] = nums1_copy[p1]
            p1 += 1
         else:
            nums1[p] = nums2[p2]
            p2 += 1
