from django.http import HttpResponse
from django.shortcuts import redirect, render

from weight_tracker.models import Weight

def home_page(request):
    new_weight = request.POST.get('new_weight', None)
    if new_weight:
        Weight.objects.create(value=new_weight)
        return redirect('Home')
    weights = Weight.objects.all()
    return render(request, 'home.html', {'weights': weights})
