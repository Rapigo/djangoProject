from django.shortcuts import render

# Create your views here.
from myApp.models import Emp


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_emps = Emp.objects.all().count()


    context = {
        'num_emps': num_emps
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

from django.views import generic

class EmployeeListView(generic.ListView):
    model = Emp

class EmployeeDetailView(generic.DetailView):
    model = Emp