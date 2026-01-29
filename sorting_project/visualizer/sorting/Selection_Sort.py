from .base import SortingAlgorithm

class SelectionSort(SortingAlgorithm):
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
            min_idx = i
            # Record first comparison of this pass
            self.steps.append({
                'array': self.data.copy(),
                'comparing_indices': [i],
                'swapped_indices': [],
                'sorted_indices': list(range(i)),
                'description': f'Pass {i+1}: Finding minimum starting from index {i}'
            })
            
            for j in range(i+1, n):
                # Record each comparison
                self.steps.append({
                    'array': self.data.copy(),
                    'comparing_indices': [i, j],
                    'swapped_indices': [],
                    'sorted_indices': list(range(i)),
                    'description': f'Comparing indices {i} ({self.data[i]}) and {j} ({self.data[j]})'
                })
                
                if self.data[j] < self.data[min_idx]:
                    min_idx = j
            
            # Swap if needed
            if min_idx != i:
                self.data[i], self.data[min_idx] = self.data[min_idx], self.data[i]
                # Record swap step
                self.steps.append({
                    'array': self.data.copy(),
                    'comparing_indices': [],
                    'swapped_indices': [i, min_idx],
                    'sorted_indices': list(range(i+1)),
                    'description': f'Swapped indices {i} and {min_idx}. Element {self.data[i]} is now in its correct position.'
                })
            else:
                # Record when element is already in correct position
                self.steps.append({
                    'array': self.data.copy(),
                    'comparing_indices': [],
                    'swapped_indices': [],
                    'sorted_indices': list(range(i+1)),
                    'description': f'Element at index {i} is already in its correct position.'
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
