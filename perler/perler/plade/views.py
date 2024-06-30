from django.shortcuts import render, redirect
from django.views import View
from .models import Plade, Runde, Category, Kant

# Create your views here.
class Index(View):
    def get(self, request, *args, **kwargs):
      hjerter = Plade.objects.filter(category__name__contains = 'Hjerter')
      stjerne = Plade.objects.filter(category__name__contains = 'Stjerne')
      jul = Plade.objects.filter(category__name__contains = 'Jul')
      andet = Plade.objects.filter(category__name__contains = 'Andet')
      hjerte = Plade.objects.filter(kant__name__contains = 'Hjerte')
      stjern = Plade.objects.filter(kant__name__contains = 'Stjerne')
      rund = Plade.objects.filter(kant__name__contains = 'Rund')
      firkant = Plade.objects.filter(kant__name__contains = 'firkant')
      sekskant = Plade.objects.filter(kant__name__contains = 'sekskant')
      context = {
          'stjerne': stjerne,
          'hjerter': hjerter,
          'jul': jul,
          'andet': andet,
          'hjerte': hjerte,
          'rund': rund,
          'firkant': firkant,
          'sekskant': sekskant,
          'stjern': stjern,
        } 
      return render(request, 'plade/index.html', context)
