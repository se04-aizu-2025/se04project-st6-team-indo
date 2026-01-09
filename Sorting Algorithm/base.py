from abc import ABC, abstractmethod

class SortingAlgorithm(ABC):
    def __init__(self, data):
        self.data = data

    @abstractmethod
    def sort(self):
        """Sort the data and return it."""
        pass

    def display(self):
        print(f"{self.__class__.__name__} Result: {self.data}")