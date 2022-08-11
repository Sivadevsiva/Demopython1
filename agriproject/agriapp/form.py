from django import forms
from . models import Agri

class Agriform(forms.ModelForm):
    class Meta:
        model=Agri
        fields=['name','use','About','img']