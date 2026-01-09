from Bubble_Sort import bubbleSort
from Selection_Sort import selectionSort
from insertion_sort import insertionSort
from merge_sort import mergeSort
from quick_sort import quickSort
from Heap_Sort import heapSort

from data_engineer import DataEngineer
from base import FunctionSortAdapter
from test_engine import SortingTestEngine


def main():
    data_engineer = DataEngineer(size=50, seed=42)
    base_data = data_engineer.generate()

    print(f"Original Array:\n{base_data}\n")

    algorithms = [
        FunctionSortAdapter(base_data.copy(), bubbleSort),
        FunctionSortAdapter(base_data.copy(), selectionSort),
        FunctionSortAdapter(base_data.copy(), insertionSort),
        FunctionSortAdapter(base_data.copy(), mergeSort),
        FunctionSortAdapter(base_data.copy(), quickSort),
        FunctionSortAdapter(base_data.copy(), heapSort),
    ]

    test_engine = SortingTestEngine(algorithms)
    test_engine.run()


if __name__ == "__main__":
    main()
