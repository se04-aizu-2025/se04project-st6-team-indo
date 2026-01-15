class SortingTestEngine:
    def __init__(self, algorithms):
        self.algorithms = algorithms

    def run(self):
        print("\n=== Running Sorting Tests ===")
        for algorithm in self.algorithms:
            result = algorithm.sort()
            assert result == sorted(result), "Sorting failed!"
            algorithm.display()
        print("All sorting algorithms passed.\n")
