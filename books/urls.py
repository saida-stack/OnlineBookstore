from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.BooksListView.as_view(), name='books_list'),
    path('detail/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('create/', views.BookCreateView.as_view(), name='book_create'),
    path('update/<int:pk>/', views.BookUpdateView.as_view(), name='book_update'),
    path('delete/<int:pk>/', views.BookDeleteView.as_view(), name='book_delete'),
]