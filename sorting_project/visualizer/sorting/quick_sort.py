from .base import SortingAlgorithm

class QuickSort(SortingAlgorithm):

    def sort(self):
        self.steps = []
        self.sorted_indices = set()
        self._quick_sort(0, len(self.data) - 1)
        return self.data

    def _quick_sort(self, low, high):
        if low < high:
            pi = self._partition(low, high)
            self.sorted_indices.add(pi)

            self._quick_sort(low, pi - 1)
            self._quick_sort(pi + 1, high)

        elif low == high:
            self.sorted_indices.add(low)

    def _partition(self, low, high):
        pivot_index = high
        pivot = self.data[pivot_index]
        i = low - 1

        self._record_step(
            pivot_index=pivot_index,
            left_indices=[],
            right_indices=list(range(low, high))
        )

        for j in range(low, high):
            if self.data[j] <= pivot:
                i += 1
                self.data[i], self.data[j] = self.data[j], self.data[i]

        self.data[i + 1], self.data[high] = self.data[high], self.data[i + 1]
        pivot_final_index = i + 1

        self._record_step(
            pivot_index=pivot_final_index,
            left_indices=list(range(low, pivot_final_index)),
            right_indices=list(range(pivot_final_index + 1, high + 1))
        )

        return pivot_final_index

    def _record_step(self, pivot_index, left_indices, right_indices):
        self.steps.append({
            "array": self.data.copy(),
            "pivot_index": pivot_index,
            "left_indices": left_indices,
            "right_indices": right_indices,
            "sorted_indices": list(self.sorted_indices)
        })
