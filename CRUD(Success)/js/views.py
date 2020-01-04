from django.shortcuts import render
from .models import Color
from .forms import ColorForm
 
 
def index(request):
    d = {
        'colors': Color.objects.all(),
        'form': ColorForm(),
    }
    return render(request, 'js/index.html', d)