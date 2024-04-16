from django.urls import reverse_lazy
from django.views import generic
from .models import Book
from .forms import BookForm


class BooksListView(generic.ListView):
    model = Book
    template_name = 'books/books_list.html'

    def get_queryset(self):
        return Book.objects.order_by('-date_modified')


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'


class BookCreateView(generic.CreateView):
    model = Book
    template_name = 'books/book_create.html'
    form_class = BookForm


class BookUpdateView(generic.UpdateView):
    model = Book
    template_name = 'books/book_create.html'
    form_class = BookForm


class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('books_list')
