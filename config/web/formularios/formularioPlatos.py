# los formularios de Django son clases 

from django import forms

#Hereda
class FormularioPlatos(forms.Form):
    #Creando atributo parta cargar el select (choicefield)
    OPCIONES = (
        (1, 'Entrada'),
        (2, 'Plato fuerte'),
        (3, 'Postre'),
    )

    #Dentro de la clase, cada atributo será un input

    nombrePlato = forms.CharField(
        #tipo de input y atributos dentro de diccionario
        widget= forms.TextInput(attrs={'class': 'form-control mb-3'}),
        label='Nombre del plato',
        required=True,
        max_length=5
    )

    descripcionPlato = forms.CharField(
        widget= forms.TextInput(attrs={'class': 'form-control mb-3'}),
        label='Descripcion',
        required=False,
        max_length=20
    )

    precioPlato = forms.CharField(
        widget= forms.NumberInput(attrs={'class': 'form-control mb-3'}),
        label='Precio',
        required=True,
    )

    tipoPlato = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control mb-3'}),
        required=True,
        label='Tipo de plato',
        choices=OPCIONES
    )

    fotoPlato = forms.CharField(
        widget= forms.TextInput(attrs={'class': 'form-control mb-3'}),
        required=True,
        label='Foto',
    )

