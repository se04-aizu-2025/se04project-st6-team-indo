from base import SortingAlgorithm

class SelectionSort(SortingAlgorithm):
    def sort(self):
        n = len(self.data)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if self.data[j] < self.data[min_idx]:
                    min_idx = j
            self.data[i], self.data[min_idx] = self.data[min_idx], self.data[i]
        return self.data