from django.shortcuts import render
from django.http import HttpResponse
from .models import Uslugi
from django.utils import timezone

def uslugi(request):
    uslugis = Uslugi.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'uslugi/uslugi.html', {"uslugis": uslugis})


