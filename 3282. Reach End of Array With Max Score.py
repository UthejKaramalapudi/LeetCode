class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        total_score = 0
        max_value = 0
        n = len(nums)

        for i in range(n - 1):
            max_value = max(max_value, nums[i])
            total_score += max_value

        return total_score                    
