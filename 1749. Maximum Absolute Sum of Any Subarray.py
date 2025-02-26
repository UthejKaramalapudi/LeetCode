class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        curr_sum = 0
        min_sum = 0
        max_sum = 0

        for num in nums:
            curr_sum += num
            min_sum = min(min_sum, curr_sum)
            max_sum = max(max_sum, curr_sum)

        abs_maxSum = abs(max_sum - min_sum)
        return abs_maxSum
