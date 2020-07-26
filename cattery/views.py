from django.shortcuts import render
from django.utils import timezone
from .models import CatCard


def cat_list(request):
    cats = CatCard.objects.all()
    return render(request, './pets.html', {'cats': cats})







