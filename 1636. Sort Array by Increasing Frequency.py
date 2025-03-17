class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        hash_map = {}

        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1

        nums.sort(key=lambda x: (hash_map[x], -x))
        
        return nums
