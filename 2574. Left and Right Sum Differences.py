class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        # leftSum, rightSum = [], []
        # curr_leftSum, curr_rightSum = 0, 0
        # answer = []
        # n = len(nums)

        # for i in range(n):
        #     leftSum.append(curr_leftSum)
        #     curr_leftSum += nums[i]

        # for i in range(n-1, -1, -1):
        #     rightSum.append(curr_rightSum)
        #     curr_rightSum += nums[i]
        # rightSum = rightSum[::-1]

        # for i in range(n):
        #     answer.append(abs(leftSum[i] - rightSum[i]))

        # return answer

        n = len(nums)
        total_sum = sum(nums)
        left_sum = 0
        answer = []

        for i in range(n):
            right_sum = total_sum - left_sum - nums[i]
            answer.append(abs(left_sum - right_sum))
            left_sum += nums[i]

        return answer
