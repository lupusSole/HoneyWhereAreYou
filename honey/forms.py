from django.forms import ModelForm
from .models import Contact
from django import forms


class ContactForm(ModelForm):
    email = forms.EmailField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    subject = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    message = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Contact
        fields = ('email', 'subject', 'message')