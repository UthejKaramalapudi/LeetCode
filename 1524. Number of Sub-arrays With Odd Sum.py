class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        # Brute - Force Method

        # MOD = 1e9 + 7
        # n = len(arr)
        # count = 0

        # for i in range(n):
        #     currSum = 0
        #     for j in range(i, n):
        #         currSum += arr[j]

        #         if currSum % 2 != 0:
        #             count += 1

        # return int(count % MOD)

        MOD = 1e9 + 7
        count = 0
        prefix_sum = 0
        odd_sum = 0
        even_sum = 1

        for num in arr:
            prefix_sum += num
            if prefix_sum % 2 == 0:
                count += odd_sum
                even_sum += 1
            else:
                count += even_sum
                odd_sum += 1
            
        return int(count % MOD)
