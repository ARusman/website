from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from .models import Capital

def index(request):
    all_capitals = Capital.objects.all()
    context = {'all_capitals': all_capitals}
    return render(request, 'co2/index.html', context)

def detail(request, capital_id):
    return HttpResponse("<h2>Details for Capital id: " + str(capital_id) + "</h2>")
