from django import forms
from .models import Posteo

class PosteoForm(forms.ModelForm):
    class Meta:
        model = Posteo
        fields = ['titulo', 'subtitulo', 'contenido', 'imagen', 'autor',]

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escriba un título hasta 60 caracteres'}),
            'subtitulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escriba un subtítulo hasta 120 caracteres'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Agregue el contenido'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'autor': forms.Select(attrs={'class': 'form-control'}),
            
        }

class ContactoForm(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escriba su nombre'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Escriba su email'}))
    telefono = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escriba su teléfono'}))
    mensaje = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escriba su mensaje'}))

