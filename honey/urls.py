from django.urls import path
from . import views

urlpatterns = [
    # home
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name="contact"),


 

    ]