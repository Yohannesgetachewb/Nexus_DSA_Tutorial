class Solution:
    def largestNumber(self, nums: list[int]) -> str:

        strs = list(map(str, nums))
        def compare(x: str, y: str) -> int:
            if x + y > y + x:
                return -1  
            elif x + y < y + x:
                return 1   
            else:
                return 0
        strs.sort(key=cmp_to_key(compare))
        if strs[0] == "0":
            return "0"
            
        return "".join(strs)
