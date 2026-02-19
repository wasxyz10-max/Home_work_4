from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('book_citations/', views.BookCitationsView.as_view(), name='book_citations'),
    path('book_search/', views.SearchBookView.as_view(), name='search_book'),
    path('book_detail/<int:id>/', views.BookDetailView.as_view(), name='book_detail'),
    path('book/', views.BookListView.as_view(), name='book_user'),
    path('book_update/<int:id>/', views.UpdateBookView.as_view(), name='update_book'),
    path('book_create/', views.CreateBookView.as_view(), name='create_book'),
    path('book_delete/<int:id>/', views.DeleteBookView.as_view(), name='delete_book'),
]