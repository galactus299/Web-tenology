import re
from django.shortcuts import render
from .models import movies
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
# Create your views here.

from django.views import generic

class MovieListView(generic.ListView):
    model = movies
    template_name = 'movies/index.html'
   
def delete(request, id):
  movie = movies.objects.get(id=id)
  movie.delete()
  return HttpResponseRedirect(reverse('movies'))   
def update(request, id):
  mymember = movies.objects.get(id=id)
  template = loader.get_template('movies/update.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  Moviename = request.POST.get('Moviename',False)
  Summary= request.POST.get('Summary',False)
  Actorname=request.POST.get('Actorname',False)
  Releasedate=request.POST.get('Releasedate',False)
  movie = movies.objects.get(id=id)
  
  movie.movie_name = Moviename
  movie.summary = Summary
  movie.Actorname=Actorname
#   movie.release_date=Releasedate
  movie.save()

  return HttpResponseRedirect(reverse('movies'))
