from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from .models import Capital

def index(request):
    all_capitals = Capital.objects.all()
    template = loader.get_template('co2/index.html')
    context = {
        'all_capitals': all_capitals,
    }
    return HttpResponse(template.render(context, request))

def detail(request, capital_id):
    return HttpResponse("<h2>Details for Capital id: " + str(capital_id) + "</h2>")
