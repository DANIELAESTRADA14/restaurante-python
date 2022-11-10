from django.shortcuts import render
from web.formularios.formularioPlatos import FormularioPlatos
from web.formularios.formularioRegistro import FormularioRegistros
from web.models import Platos, Empleados

# Create your views here.
def Home(request):
    return render(request, 'index.html')

def VistaPlatos(request):
    formulario = FormularioPlatos()
    #Variable tipo diccionario envia info al template
    datosParaTemplate = {
        'formularioPlatos': formulario,
        'bandera': False
    }
    
    # Preguntamos si existe alguna petición de tipo POST asociada a la vista
    if request.method == 'POST':
        # Debemos camputar los datos del formulario
        datosDelFormulario = FormularioPlatos(request.POST)
        # Verificar sí los datos llegaron correctamente (VALIDACIONES)
        if datosDelFormulario.is_valid():
            # Capturamos la data
            datosPlato = datosDelFormulario.cleaned_data
            # Hay que encapsular datosPlatos en el modelo, creamos objeto de tipo modelo Plato
            platoNuevo = Platos(
                nombre = datosPlato["nombrePlato"],
                descripcion = datosPlato["descripcionPlato"],
                foto = datosPlato["fotoPlato"],
                precio = datosPlato["precioPlato"],
                tipo = datosPlato["tipoPlato"],
            )
            #Intentamos llevar objeto a bd
            try:
                platoNuevo.save()
                datosParaTemplate['bandera'] = True
            except Exception as error:
                datosParaTemplate['bandera'] = False
                print(f'error: {error}')

    return render(request, 'platos.html', datosParaTemplate)

def Personal(request):
    registro = FormularioRegistros()
    datosParaTemplate2 = {
        'formularioRegistro': registro,
        'bandera': False
    }

    if request.method == 'POST':
        datosDelFormulario = FormularioRegistros(request.POST)
        if datosDelFormulario.is_valid():
            datosPersonal = datosDelFormulario.cleaned_data
            empleadoNuevo = Empleados(
                nombre = datosPersonal['nombre'],
                apellidos = datosPersonal['apellido'],
                foto = datosPersonal['fotoEmpleado'],
                cargo = datosPersonal['cargo'],
                salario = datosPersonal['salario'],
                contacto = datosPersonal['contacto'],
            )
            try:
                empleadoNuevo.save()
                datosParaTemplate2['bandera'] = True
            except Exception as error:
                datosParaTemplate2['bandera'] = False
                print(f'error: {error}')

    return render(request, 'personal.html', datosParaTemplate2)
