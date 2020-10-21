from django.urls import path     
from . import views
urlpatterns = [
    path('', views.addBook),
    path('authors', views.addAuthor),	
    path('books/<int:book_id>', views.displayBook),
    path('authors/<int:author_id>', views.displayAuthor),   
]