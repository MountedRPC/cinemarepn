from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from home.models import Films



def Homepage(request):
    film = Films.objects.all()[:8]
    return render(request, 'home/index.html', {'films': film})


