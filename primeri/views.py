from django.shortcuts import render
from .models import PrimerImage

def raboti(request):
    raboti = PrimerImage.objects.all()
    return render(request, 'primer_rabot/primer_rabot.html', {"raboti": raboti})


