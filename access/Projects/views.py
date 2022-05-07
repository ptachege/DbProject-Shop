from django.shortcuts import render


def landing_page(request):
    return render(request, 'Projects/home.html')


def contact(request):
    return render(request, 'Projects/contactus.html')
