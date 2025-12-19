from base import SortingAlgorithm

class HeapSort(SortingAlgorithm):
    def heapify(self, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and self.data[left] > self.data[largest]:
            largest = left
        if right < n and self.data[right] > self.data[largest]:
            largest = right

        if largest != i:
            self.data[i], self.data[largest] = self.data[largest], self.data[i]
            self.heapify(n, largest)

    def sort(self):
        n = len(self.data)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(n, i)
        for i in range(n - 1, 0, -1):
            self.data[i], self.data[0] = self.data[0], self.data[i]
            self.heapify(i, 0)
        return self.data