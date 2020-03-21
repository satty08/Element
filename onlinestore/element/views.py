from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView
from .forms import BookForm
from . import forms
from .models import book
# Create your views here.

class HomePage(TemplateView):
    template_name = 'home.html'



def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render (request, 'upload.html', context)

def book_list(request):
    books = book.objects.all()
    return render(request, 'book_list.html', {
        'books': books
    })

def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'upload_book.html', {
        'form':form
    })

def delete_book(request,pk):
    if request.method  == "POST":
        Book = book.objects.get(pk=pk)
        Book.delete()
    return redirect('book_list')
