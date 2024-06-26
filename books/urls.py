from django.urls import path
from books.views import books, book_details

urlpatterns = [
    path("books/", books, name="books"),
    path("book-detail/", book_details, name="book-detail")
]


# argument type : slug, int, str

# argument strukturasi <turi:nomi>