class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0

        for num in range(low, high + 1):
            num = list(str(num))

            if len(num) % 2 == 0:
                first_sum, last_sum = 0, 0
                mid = len(num) // 2

                for i in num[:mid]:
                    first_sum += int(i)

                for j in num[mid:]:
                    last_sum += int(j)

                if first_sum == last_sum:
                    count += 1

        return count
