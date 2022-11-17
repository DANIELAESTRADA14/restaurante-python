from django.shortcuts import render
from django.shortcuts import redirect
from web.formularios.formularioPlatos import FormularioPlatos
from web.formularios.formularioRegistro import FormularioRegistros
from web.formularios.formularioEdicionPlatos import FomularioEdicionPlatos
from web.models import Platos, Empleados

# Create your views here.
def Home(request):
    return render(request, 'index.html')

def MenuPlatos(request):
    # Traer datos de db
    platosConsultados = Platos.objects.all()
    formulario = FomularioEdicionPlatos()
    # Llevarlos al template
    diccionarioEnvio={
        'platos': platosConsultados,
        'formulario': formulario
    }

    return render(request, 'menuPlatos.html', diccionarioEnvio)

def MenuPersonal(request):
    personalConsultado = Empleados.objects.all()
    for empleado in personalConsultado:
        tipo = empleado.cargo
        if tipo == 1:
            empleado.cargo = 'Cocinero'
    diccionarioPersonal={
        'personas': personalConsultado
    }
    return render(request, 'menuPersonal.html', diccionarioPersonal)

def EditarPlatos(request, id):
    # Recibir datos del formulario y editar 
    print(id)
    if request.method == 'POST':
        datosDelFormulario = FomularioEdicionPlatos(request.POST)
        if datosDelFormulario.is_valid():
            datosPlato = datosDelFormulario.cleaned_data
            try:
                Platos.objects.filter(pk=id).update(precio=datosPlato['precioPlato'])
                print('Exito guardando')
            except Exception as error:
                
                print(f'error: {error}')
             
    return redirect('menu')


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
