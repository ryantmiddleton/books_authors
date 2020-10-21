from django.shortcuts import render, redirect
from books_authors_app.models import Book, Author
# Create your views here.
def addBook(request):
    if request.method =="POST":
        Book.objects.create(
            title=request.POST['book_title_txt'],
            desc=request.POST['book_desc_txt']
        )
        return redirect("")
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'add_book.html', context)

def addAuthor(request):
    if request.method =="POST":
        Author.objects.create(
            first_name=request.POST['first_name_txt'],
            last_name=request.POST['last_name_txt'],
            notes=request.POST['notes_txt']
        )
        return redirect("/authors")
    context = {
        'authors': Author.objects.all()
    }
    return render(request, 'add_author.html', context)

def displayBook(request, book_id):
    disp_book = Book.objects.get(id=book_id)
    if request.method=="POST":
        add_author = Author.objects.get(id=request.POST['add_author_sel'])
        disp_book.authors.add(add_author)
        return redirect("/books/"+str(book_id))

    context = {
        'id':book_id,
        'book_title':disp_book.title,
        'book_desc':disp_book.desc,
        'authors':disp_book.authors.all(),
        'alt_authors':Author.objects.exclude(books__id=book_id)
    }
    return render(request, 'display_book.html', context)

def displayAuthor(request, author_id):
    disp_author = Author.objects.get(id=author_id)
    if request.method=="POST":
        add_book = Book.objects.get(id=request.POST['add_book_sel'])
        disp_author.books.add(add_book)
        return redirect("/authors/"+str(author_id))

    context = {
        'id':author_id,
        'first_name':disp_author.first_name,
        'last_name':disp_author.last_name,
        'notes':disp_author.notes,
        'books':disp_author.books.all(),
        'alt_books':Book.objects.exclude(authors__id=author_id)
    }
    return render(request, 'display_author.html', context)