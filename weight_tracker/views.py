from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    new_weight = request.POST.get('new_weight', '')
    return render(request, 'home.html', {'new_weight': new_weight})
