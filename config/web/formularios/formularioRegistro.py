# los formularios de Django son clases 

from django import forms

#Hereda
class FormularioRegistros(forms.Form):
    OPCIONES = (
        (1, 'Cocinero'),
        (2, 'Ayudante'),
        (3, 'Mesero'),
        (4, 'Admin'),
    )

    #Dentro de la clase, cada atributo será un input

    nombre = forms.CharField(
        #tipo de input y atributos dentro de diccionario
        widget= forms.TextInput(attrs={'class': 'form-control my-3'}),
        required=True,
        label='Nombre',
        max_length=30
    )

    apellido = forms.CharField(
        #tipo de input y atributos dentro de diccionario
        widget= forms.TextInput(attrs={'class': 'form-control my-3'}),
        required=True,
        label='Apellido',
        max_length=30
    )

    fotoEmpleado = forms.CharField(
        widget= forms.TextInput(attrs={'class': 'form-control mb-3'}),
        required=True,
        label='Foto',
    )

    cargo = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control mb-3'}),
        required=True,
        label='Cargo',
        choices=OPCIONES
    )

    salario = forms.CharField(
        widget= forms.NumberInput(attrs={'class': 'form-control mb-3'}),
        required=True,
    )

    contacto = forms.CharField(
        widget=forms.NumberInput(attrs={'class': 'form-control mb-3'}),
        required=True,
    )

    

