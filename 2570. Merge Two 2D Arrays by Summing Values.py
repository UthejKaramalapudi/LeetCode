class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        res_arr = []
        i, j = 0, 0
        n, m = len(nums1), len(nums2)

        while i < n and j < m:
            if nums1[i][0] == nums2[j][0]:
                id_sum = nums1[i][1] + nums2[j][1]
                res_arr.append([nums1[i][0], id_sum])
                i += 1
                j += 1
            elif nums1[i][0] < nums2[j][0]:
                res_arr.append([nums1[i][0], nums1[i][1]])
                i += 1
            elif nums1[i][0] > nums2[j][0]:
                res_arr.append([nums2[j][0], nums2[j][1]])
                j += 1

        while i < n:
            res_arr.append(nums1[i])
            i += 1

        while j < m:
            res_arr.append(nums2[j])
            j += 1

        return res_arr
