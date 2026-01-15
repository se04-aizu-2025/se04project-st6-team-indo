from Bubble_Sort import BubbleSort
from Selection_Sort import SelectionSort
from insertion_sort import InsertionSort
from merge_sort import MergeSort
from quick_sort import QuickSort
from Heap_Sort import HeapSort

from data_engineer import DataEngineer
from test_engine import SortingTestEngine


def main():
    data_engineer = DataEngineer(size=10, seed=42)
    base_data = data_engineer.generate()

    print(f"Original Array:\n{base_data}\n")

    algorithms = [
        BubbleSort(base_data.copy()),
        SelectionSort(base_data.copy()),
        InsertionSort(base_data.copy()),
        MergeSort(base_data.copy()),
        QuickSort(base_data.copy()),
        HeapSort(base_data.copy()),
    ]

    test_engine = SortingTestEngine(algorithms)
    test_engine.run()


if __name__ == "__main__":
    main()
