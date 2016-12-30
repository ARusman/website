from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Capital

class IndexView(generic.ListView):
    template_name = 'co2/index.html'
    context_object_name = 'all_capitals'

    def get_queryset(self):
        return Capital.objects.all()

class DetailView(generic.DetailView):
    model = Capital
    template_name = 'co2/detail.html'

class CapitalCreate(CreateView):
    model = Capital
    fields = ['color', 'capital_title']

