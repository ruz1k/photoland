from django.shortcuts import render
from .models import Shablon

def index(request):
    shab = Shablon.objects.all()
    return render (request, 'shablon/index.html', {"shab": shab})
