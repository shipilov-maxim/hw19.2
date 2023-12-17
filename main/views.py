from django.shortcuts import render


# Create your views here.

def catalog(request):
    return render(request, 'main/catalog.html')


def contact(request):
    return render(request, 'main/contact.html')
