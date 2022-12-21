from django.contrib import admin
from django.urls import path
from .views import bookListView,bookDetailView,libraryListView,libraryDetailView

urlpatterns = [
   path('', bookListView.as_view(), name='book_list'),
   path('<int:pk>', bookDetailView.as_view(),name='book_detail'),
   path('libraries/', libraryListView.as_view(), name='library_list'),
   path('libraries/<int:pk>', libraryDetailView.as_view(),name='library_detail')
    
]