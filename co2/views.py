from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import  reverse_lazy
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

class CapitalUpdate(UpdateView):
    model = Capital
    fields = ['color', 'capital_title']

class CapitalDelete(DeleteView):
    model = Capital
    success_url = reverse_lazy('co2:index')

