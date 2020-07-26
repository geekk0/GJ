from django.shortcuts import render


def welcome_text(request):
    return render(request, 'main.html')


def contacts(request):
    return render(request, 'contacts.html')


def about(request):
    return render(request, 'about.html')


def pets(request):
    return render(request, 'pets.html')


