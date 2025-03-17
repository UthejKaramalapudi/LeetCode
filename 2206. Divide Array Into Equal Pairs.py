class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hash_map = {}

        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1

        for freq in hash_map.values():
            if freq % 2 != 0:
                return False

        return True
