from django import forms

class FomularioEdicionPlatos(forms.Form):

        precioPlato = forms.CharField(
        widget= forms.NumberInput(attrs={'class': 'form-control mb-3'}),
        label='Precio',
        required=True,
    )

class FormularioEdicionSalario(forms.Form):
    
    salario = forms.CharField(
        widget= forms.NumberInput(attrs={'class': 'form-control mb-3'}),
        required=True,
    )
