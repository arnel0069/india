# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('destinations/', views.destinations, name='destinations'),
    path('culture/', views.culture, name='culture'),
    path('contact-us/', views.contact_us, name='contact_us'),
]
