class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        x, y = 0, 0
        temp = 0

        for diff in differences:
            temp += diff
            x = min(x, temp)
            y = max(y, temp)

            if (y - x) > (upper - lower):
                return 0

        return (upper - lower) - (y - x) + 1
