from base import SortingAlgorithm

class MergeSort(SortingAlgorithm):
    def sort(self):
        self.data = self._merge_sort(self.data)
        return self.data

    def _merge_sort(self, arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr)//2
        left = self._merge_sort(arr[:mid])
        right = self._merge_sort(arr[mid:])
        return self._merge(left, right)

    def _merge(self, left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result