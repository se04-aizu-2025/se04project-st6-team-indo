from django.shortcuts import render
from .sorting.Bubble_Sort import BubbleSort
from .sorting.merge_sort import MergeSort
from .sorting.Heap_Sort import HeapSort
from .sorting.insertion_sort import InsertionSort
from .sorting.quick_sort import QuickSort
from .sorting.Selection_Sort import SelectionSort
from .sorting.data_engineer import DataEngineer

# opens respective pages when clicking on button at the land page
def landing_page(request):
    return render(request, 'land_page.html')

def bubble_sort(request):
    return render(request, 'bubble_page.html')

def merge_sort(request):
    return render(request, 'merge_page.html')

def quick_sort(request):
    return render(request, 'quick_page.html')

def heap_sort(request):
    return render(request, 'heap_page.html')

def insertion_sort(request):
    return render(request, 'insert_page.html')

def selection_sort(request):
    return render(request, 'selection_page.html')


# respective functions for each sorting page
def bubble_sort_view(request):
    numbers_original = []
    sorted_data = None

    if request.method == "POST":
        if "randomize" in request.POST:
            data_engineer = DataEngineer(size=10, seed=None)
            numbers_original = data_engineer.generate()
        elif "sort" in request.POST:
            input_numbers = request.POST.get("numbers_array", "")
            numbers_original = [int(x) for x in input_numbers.strip().split()]
            sorter = BubbleSort(numbers_original.copy())  
            sorted_data = sorter.sort()

    return render(request, "bubble_page.html", {
        "numbers": numbers_original,  
        "sorted_data": sorted_data     
    })
    
def merge_sort_view(request):
    numbers_original = []
    sorted_data = None

    if request.method == "POST":
        if "randomize" in request.POST:
            data_engineer = DataEngineer(size=10, seed=None)
            numbers_original = data_engineer.generate()
        elif "sort" in request.POST:
            input_numbers = request.POST.get("numbers_array", "")
            numbers_original = [int(x) for x in input_numbers.strip().split()]
            sorter = MergeSort(numbers_original.copy())  
            sorted_data = sorter.sort()

    return render(request, "merge_page.html", {
        "numbers": numbers_original,  
        "sorted_data": sorted_data     
    })

def heap_sort_view(request):
    numbers_original = []
    sorted_data = None

    if request.method == "POST":
        if "randomize" in request.POST:
            data_engineer = DataEngineer(size=10, seed=None)
            numbers_original = data_engineer.generate()
        elif "sort" in request.POST:
            input_numbers = request.POST.get("numbers_array", "")
            numbers_original = [int(x) for x in input_numbers.strip().split()]
            sorter = HeapSort(numbers_original.copy())  
            sorted_data = sorter.sort()

    return render(request, "heap_page.html", {
        "numbers": numbers_original,  
        "sorted_data": sorted_data     
    })

def insertion_sort_view(request):
    numbers_original = []
    sorted_data = None

    if request.method == "POST":
        if "randomize" in request.POST:
            data_engineer = DataEngineer(size=10, seed=None)
            numbers_original = data_engineer.generate()
        elif "sort" in request.POST:
            input_numbers = request.POST.get("numbers_array", "")
            numbers_original = [int(x) for x in input_numbers.strip().split()]
            sorter = InsertionSort(numbers_original.copy())  
            sorted_data = sorter.sort()

    return render(request, "insertion_page.html", {
        "numbers": numbers_original,  
        "sorted_data": sorted_data     
    })

def quick_sort_view(request):
    numbers_original = []
    sorted_data = None

    if request.method == "POST":
        if "randomize" in request.POST:
            data_engineer = DataEngineer(size=10, seed=None)
            numbers_original = data_engineer.generate()
        elif "sort" in request.POST:
            input_numbers = request.POST.get("numbers_array", "")
            numbers_original = [int(x) for x in input_numbers.strip().split()]
            sorter = QuickSort(numbers_original.copy())  
            sorted_data = sorter.sort()

    return render(request, "quick_page.html", {
        "numbers": numbers_original,  
        "sorted_data": sorted_data     
    })

def selection_sort_view(request):
    numbers_original = []
    sorted_data = None

    if request.method == "POST":
        if "randomize" in request.POST:
            data_engineer = DataEngineer(size=10, seed=None)
            numbers_original = data_engineer.generate()
        elif "sort" in request.POST:
            input_numbers = request.POST.get("numbers_array", "")
            numbers_original = [int(x) for x in input_numbers.strip().split()]
            sorter = SelectionSort(numbers_original.copy())  
            sorted_data = sorter.sort()

    return render(request, "selection_page.html", {
        "numbers": numbers_original,  
        "sorted_data": sorted_data     
    })


    



