class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        hash_map = {}

        for i in range(n):
            for j in range(n):
                if grid[i][j] not in hash_map:
                    hash_map[grid[i][j]] = 1
                else:
                    hash_map[grid[i][j]] += 1

        for num in range(1, n*n+1):
            if num not in hash_map:
                missed = num
            elif hash_map[num] == 2:
                repeated = num

        return [repeated, missed]
