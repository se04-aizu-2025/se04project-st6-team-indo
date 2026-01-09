import numpy as np

class DataEngineer:
    def __init__(self, size=50, low=0, high=100, seed=None):
        self.size = size
        self.low = low
        self.high = high
        self.seed = seed

    def generate(self):
        if self.seed is not None:
            np.random.seed(self.seed)
        return np.random.randint(self.low, self.high, size=self.size).tolist()
