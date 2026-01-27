from .base import SortingAlgorithm

class MergeSort(SortingAlgorithm):
    def sort(self):
        self.steps = []              
        arr = self.data.copy()
        self._divide(arr)
        self.data = sorted(arr)      
        return self.data

    def get_steps(self):
        if not hasattr(self, "steps"):
            self.sort()
        return self.steps

    def _divide(self, arr):
        if len(arr) <= 1:
            return

        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        
        self.steps.append({
            "left": left.copy(),
            "right": right.copy()
        })

        self._divide(left)
        self._divide(right)
