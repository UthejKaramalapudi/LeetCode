class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0

        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
                        count += 1

        return count
