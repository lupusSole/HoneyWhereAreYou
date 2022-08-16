from tkinter import Image
from django.shortcuts import render
from honey.models import Update, Picture, Bio, Gallery
from .forms import ContactForm

# Create your views here.

def home(req):
    updates = Update.objects.order_by('?')[:6]
    
    # images = Picture[:6]
    context = {'updates': updates}
    return render(req, 'honey/home.html', context=context)

def about(req):
    bios = Bio.objects.all()
    galleries = Gallery.objects.all()
    context = {'bios': bios, 'galleries': galleries}
    return render(req, 'honey/about.html', context=context)

def contact(req):
    if req.method == 'POST':
        form = ContactForm(req.POST)
        if form.is_valid():
            form.save()
            return render(req, 'honey/contact.html', { 'success':"Message Sent!"})
    form = ContactForm()
    return render(req, 'honey/contact.html', {'form':form})