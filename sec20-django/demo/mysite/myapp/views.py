from django.shortcuts import render
from django.http import HttpResponse

from .models import Book #importing our books class
# Create your views here.

def index(request):
    book_list = Book.objects.all() #getting all the list of books
    context = {
        'book_list': book_list
    }
    # return HttpResponse(book_list) #after using templates, we no longer need HttpReponse, but rather render
    return render(request, 'myapp/index.html', context)


# def products(request):
#     return HttpResponse('Products') #no longer needed as we'll be displaying detailed views

def detail(request,book_id):
    # book_list = Book.objects.all()
    # mybook = book_list[book_id-1]
    # return HttpResponse("This is book number %s<br/>Price: $%s<br/>Book Name: %s<br/>Book Description: %s " % (book_id, mybook.price, mybook.name, mybook.desc))

    book = Book.objects.get(id=book_id)
    return render(request,'myapp/detail.html', {'book': book})