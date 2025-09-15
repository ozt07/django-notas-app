from django import forms

class CalculadoraForm(forms.Form):
    expresion = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingresa una expresión (ej: 2+2)',
            'id': 'expresion-input'
        })
    )