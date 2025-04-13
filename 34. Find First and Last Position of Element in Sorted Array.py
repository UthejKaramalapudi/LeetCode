class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def first_occur(nums, target):
            n = len(nums)
            l, r = 0, n - 1
            first = -1

            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    first = mid
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return first

        def last_occur(nums, target):
            n = len(nums)
            l, r = 0, n - 1
            last = -1

            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    last = mid
                    l = mid + 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return last

        return [first_occur(nums, target), last_occur(nums, target)]
