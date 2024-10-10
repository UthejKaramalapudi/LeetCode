class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        n = len(nums)

        while i <= j and j < n:
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
                j += 1
            else:
                j += 1

        while i <= n - 1:
            nums[i] = 0
            i += 1

        return nums
