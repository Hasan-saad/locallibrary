from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre

# ------------------------------------------------

from django.views.generic import CreateView 
from django.urls import reverse_lazy 
from .forms import PostForm


# ------------------------------------------------

class CreateBookView(CreateView):
     model = Book 
     form_class = PostForm
     template_name = 'create.html' 
     success_url = reverse_lazy('index')
# ------------------------------------------------



def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default.    
    num_authors = Author.objects.count()  # The 'all()' is implied by default.
    
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }
    
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

def mos(request):
    num_mos = 5858

    context = {
        'num_books': num_mos
        
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'mos.html', context=context)

def home(request):
    return render(request, 'base.html')
def other(request):
    context = {
    'k1': 'Welcome to the Second page',
    }
    return render(request, 'others.html', context)

from django.views import generic

class BookListView(generic.ListView):
    model = Book
    paginate_by = 2

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 1

class AuthorDetailView(generic.DetailView):
    model = Author
    paginate_by = 1

    
