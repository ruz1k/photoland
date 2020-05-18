from django.shortcuts import render
from .models import Uslugi

def uslugi(request):
    uslugis = Uslugi.objects.all()
    return render(request, 'uslugi/uslugi.html', {"uslugis": uslugis})


