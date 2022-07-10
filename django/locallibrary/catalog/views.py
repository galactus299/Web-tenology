from django.shortcuts import render
from .models import Book,BookInstance,Author,Genre

# Create your views here.

def index(request):
    nu_of_books= Book.objects.all().count()
    nu_of_BookInstance=BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()
    context = {
        'num_books': nu_of_books,
        'num_instances': nu_of_BookInstance,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }
    return render(request, 'index.html', context=context)


