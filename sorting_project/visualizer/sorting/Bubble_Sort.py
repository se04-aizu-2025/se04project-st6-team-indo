from .base import SortingAlgorithm

class BubbleSort(SortingAlgorithm):
    def __init__(self, data):
        super().__init__(data)
        self.steps = []  # List to store each step of the sorting process
        
    def sort(self):
        n = len(self.data)
        # Record initial state
        self.steps.append({
            'array': self.data.copy(),
            'comparing_indices': [],
            'swapped_indices': [],
            'sorted_indices': [],
            'description': 'Initial array'
        })
        
        for i in range(n):
            for j in range(0, n-i-1):
                # Record comparison step
                self.steps.append({
                    'array': self.data.copy(),
                    'comparing_indices': [j, j+1],
                    'swapped_indices': [],
                    'sorted_indices': list(range(n-i, n)),
                    'description': f'Comparing indices {j} and {j+1}: {self.data[j]} vs {self.data[j+1]}'
                })
                
                if self.data[j] > self.data[j+1]:
                    self.data[j], self.data[j+1] = self.data[j+1], self.data[j]
                    # Record swap step
                    self.steps.append({
                        'array': self.data.copy(),
                        'comparing_indices': [j, j+1],
                        'swapped_indices': [j, j+1],
                        'sorted_indices': list(range(n-i, n)),
                        'description': f'Swapped indices {j} and {j+1}'
                    })
            
            # Record when a pass is complete
            if i < n - 1:
                self.steps.append({
                    'array': self.data.copy(),
                    'comparing_indices': [],
                    'swapped_indices': [],
                    'sorted_indices': list(range(n-i-1, n)),
                    'description': f'Pass {i+1} complete. Largest element sorted.'
                })
        
        # Record final sorted state
        self.steps.append({
            'array': self.data.copy(),
            'comparing_indices': [],
            'swapped_indices': [],
            'sorted_indices': list(range(n)),
            'description': 'Sorting complete!'
        })
        
        return self.data
    
    def get_steps(self):
        """Returns the list of steps recorded during sorting"""
        return self.steps
