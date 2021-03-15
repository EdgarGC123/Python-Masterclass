from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Book #importing our books class
# Create your views here.

from .forms import BookForm

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

def add_book(request):
    if request.method == 'POST':
        # book_details = request.POST.get('name','desc','price')
        # print(book_details)
        name = request.POST.get('name',)
        desc = request.POST.get('desc',)
        price = request.POST.get('price',)
        bi = request.FILES['book_image']

        book = Book(name = name, desc = desc, price = price, book_image = bi)
        book.save()
    return render(request, 'myapp/add_book.html')

def update(request, id):
    book = Book.objects.get(id=id)
    form = BookForm(request.POST or None, request.FILES, instance=book)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'myapp/edit.html', {'form':form, 'book':book})