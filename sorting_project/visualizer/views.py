from django.shortcuts import render
from .sorting.Bubble_Sort import BubbleSort
from .sorting.merge_sort import MergeSort

from .sorting.data_engineer import DataEngineer


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



