from .base import SortingAlgorithm

class InsertionSort(SortingAlgorithm):
    def sort(self):
        for i in range(1, len(self.data)):
            key = self.data[i]
            j = i - 1
            while j >= 0 and self.data[j] > key:
                self.data[j + 1] = self.data[j]
                j -= 1
            self.data[j + 1] = key
        return self.data

    def get_steps(self):
        steps = []
        arr = self.data.copy()

        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1

            steps.append(arr.copy())

            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
                steps.append(arr.copy())

            arr[j + 1] = key
            steps.append(arr.copy())

        return steps
