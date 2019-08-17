from django.shortcuts import render
from django.http import HttpResponse
from .models import PrimerImage
from django.utils import timezone

def raboti(request):
    raboti = PrimerImage.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'primer_rabot/primer_rabot.html', {"raboti": raboti})


