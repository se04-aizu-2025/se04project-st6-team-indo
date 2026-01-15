from abc import ABC, abstractmethod

class SortingAlgorithm(ABC):
    def __init__(self, data):
        self.data = data

    @abstractmethod
    def sort(self):
        pass

    def display(self):
        print(f"{self.__class__.__name__} Result: {self.data}")


class FunctionSortAdapter(SortingAlgorithm):
    def __init__(self, data, sort_function):
        super().__init__(data)
        self.sort_function = sort_function

    def sort(self):
        result = self.sort_function(self.data)
        if result is not None:
            self.data = result
        return self.data
