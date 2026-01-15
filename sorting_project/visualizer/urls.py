from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('bubble/', views.bubble_sort, name='bubble'),
    path('merge/', views.merge_sort, name='merge'),
    path('quick/', views.quick_sort, name='quick'),
    path('heap/', views.heap_sort, name='heap'),
    path('insertion/', views.insertion_sort, name='insertion'),
    path('selection/', views.selection_sort, name='selection'),
    
    path('bubble/run/', views.bubble_sort_view, name='bubble_run'),
    #path('heap/run/', views.heap_sort_view, name='heap_run'),
    #path('insertion/run/', views.insertion_sort_view, name='insertion_run'),
    path('merge/run/', views.merge_sort_view, name='merge_run'),
    #path('quick/run/', views.quick_sort_view, name='quick_run'),
    #path('selection/run/', views.selection_sort_view, name='selection_run'),
]