from django import forms
from .models import Language, Snippet

class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields =['name','description','language','public','snippet']
        labels = {
            'name' : 'Nombre del Snippet',
            'description' : 'Descripcion',
            'language' : 'Lenguaje',
            'public' : 'Estado',
            'snippet' : 'snippet',
        }
    
