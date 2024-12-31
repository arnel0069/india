
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def destinations(request):
    return render(request, 'destinations.html')

def culture(request):
    return render(request, 'culture.html')

def cuisine(request):
    return render(request, 'cuisine.html')

def contact_us(request):
    return render(request, 'contact_us.html')

def base(request):
    return render(request,'base.html')