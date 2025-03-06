class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        weight_map = {}
        arr = []

        for value, weight in items1:
            weight_map[value] = weight_map.get(value, 0) + weight

        for value, weight in items2:
            weight_map[value] = weight_map.get(value, 0) + weight

        for value, weight in weight_map.items():
            arr.append([value, weight])

        return sorted(arr)
