

from django.shortcuts import render, get_object_or_404
from .models import Capital, Impact

def index(request):
    all_capitals = Capital.objects.all()
    return render(request, 'co2/index.html', {'all_capitals': all_capitals})

def detail(request, capital_id):
    capital = get_object_or_404(Capital, pk=capital_id)
    return render(request, 'co2/detail.html', {'capital': capital})

def favorite(request, capital_id):
    capital = get_object_or_404(Capital, pk=capital_id)
    try:
        selected_impact = capital.impact_set.get(pk=request.POST['impact'])
    except (KeyError, Impact.DoesNotExist):
        return render(request, 'co2/index.html', {
            'capital': capital,
            'error_message': "You did not select a valid impact",
        })
    else:
        selected_impact.is_favorite = True
        selected_impact.save()
        return render(request, 'co2/detail.html', {'capital': capital})
