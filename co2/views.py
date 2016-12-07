from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.shortcuts import render
from .models import Capital

def index(request):
    all_capitals = Capital.objects.all()
    return render(request, 'co2/index.html', {'all_capitals': all_capitals})

def detail(request, capital_id):
    try:
        capital = Capital.objects.get(pk=capital_id)
    except Capital.DoesNotExist:
        raise Http404("This Capital does not exist")
    return render(request, 'co2/detail.html', {'capital': capital})
