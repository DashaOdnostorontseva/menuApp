from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def catalog(request):
    return render(request, 'catalog.html')

def notebooks(request):
    return render(request, 'notebooks.html')

def phones(request):
    return render(request, 'phones.html')

def apple(request):
    return render(request, 'apple.html')

def confidentiality(request):
    return render(request, 'confidentiality.html')

def iphone17(request):
    return render(request, 'iphone17.html')

def iphone16(request):
    return render(request, 'iphone16.html')
