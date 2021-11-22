from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from home.models import Cinemas
from django.shortcuts import get_object_or_404
from django.http import Http404


def cinemas_view(request):
    cinemas = Cinemas.objects.all()
    return render(request, 'cinema/cinemas.html', {'cinemas': cinemas})


def detailcinemas(request, cinem_id):
    try:
        p = Cinemas.objects.filter(id=cinem_id)
    except Cinemas.DoesNotExist:
        raise Http404("cinem_id does not exist")
    return render(request, 'cinema/cinemaAbout.html', {'cinemas': p})
