from django import forms
from . models import Alunno

class AlunnoForm(forms.ModelForm):
    class Meta:
        model = Alunno
        fields = ['nome', 'cognome', 'email', 'telefono', 'corso'] # 'img']
