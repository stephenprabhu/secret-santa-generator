from django import forms
from django.forms import fields
from main.models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name','email']