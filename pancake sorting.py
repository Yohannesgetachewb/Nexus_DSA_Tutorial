class Solution:
    def pancakeSort(self, arr: list[int]) -> list[int]:
        res = []
        n = len(arr)

        for target in range(n, 1, -1):
            idx = arr.index(target)
            if idx == target - 1:
                continue
            if idx != 0:
                res.append(idx + 1)
                arr[: idx + 1] = reversed(arr[: idx + 1])
            res.append(target)
            arr[:target] = reversed(arr[:target])

        return res
