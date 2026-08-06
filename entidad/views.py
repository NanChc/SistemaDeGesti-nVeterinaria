from django.shortcuts import render, redirect ## el RENDER hace que se conecten la parte visual con el backend 
from django.http import HttpResponse 
import sqlite3
from .forms import AnimalForm, ClienteForm
from .models import Cliente, Animal
# Create your views here.
def index(request):
    return render(request,'entidad/index.html')

def acerca_de(request):
    return HttpResponse("CURSO")

# def animales(request, template_name='entidad/animales.html'):
#     conn = sqlite3.connect('veterinaria.sqlite')
#     animal = conn.cursor()
#     animal.execute("Select nombre, raza, categoria, dueno from animal")
#     animal_list = animal.fetchall()
#     conn.close()
#     dato = {"animales": animal_list}
#     return render(request, template_name, dato)

# def animalito(request, id_animal, template_name='entidad/animal.html'):
#     conn = sqlite3.connect('veterinaria.sqlite')
#     cursor = conn.cursor()
#     cursor.execute("select * from animal where id=?", [id_animal])
#     animal_s = cursor.fetchone()
#     dato = {"animal":animal_s}
#     return render(request, template_name, dato)

# Forms 
# def nuevo_animal(request, template_name='entidad/animal_form.html'):
#     if request.method == 'POST':
#         form = animalForm(request.POST)
#         if form.is_valid():
#             conn = sqlite3.connect('veterinaria.sqlite')
#             cursor = conn.cursor()
#             cursor.execute('Insert into animal values(?, ?, ?, ?, ?)',
#                            (form.cleaned_data['id'], form.cleaned_data['nombre'], form.cleaned_data['raza'], form.cleaned_data['categoria'], form.cleaned_data['duenio']))
#             conn.commit()
#             conn.close()
#             # return HttpResponse("El animal se ha cargado correctamente")
#             return redirect('animales')
#     else:
#         form = animalForm()
#     dato = {"form": form}
#     return render(request, template_name, dato)

# def clientes(request, template_name='entidad/clientes.html'):
#     conn = sqlite3.connect('veterinaria.sqlite')
#     cliente = conn.cursor()
#     cliente.execute("Select nombre, apellido from cliente")
#     cliente_list = cliente.fetchall()
#     conn.close()
#     dato = {"clientes": cliente_list}
#     return render(request, template_name, dato)

# def cliente(request, num_dni, template_name='entidad/cliente.html'):
#     conn = sqlite3.connect('veterinaria.sqlite')
#     cursor = conn.cursor()
#     cursor.execute("select * from cliente where num_dni=?", [num_dni])
#     cliente_s = cursor.fetchone()
#     dato = {"cliente":cliente_s}
#     return render(request, template_name, dato)

# def nuevo_cliente(request, template_name='entidad/cliente_form.html'):
#     if request.method == 'POST':
#         form = ClienteForm(request.POST)
#         if form.is_valid():
#             conn = sqlite3.connect('veterinaria.sqlite')
#             cursor = conn.cursor()
#             cursor.execute('Insert into cliente values(?, ?, ?, ?)',
#                            (form.cleaned_data['num_dni'], form.cleaned_data['nombre'], form.cleaned_data['apellido'], form.cleaned_data['direccion']))
#             conn.commit()
#             conn.close()
#             return HttpResponse("El animal se ha cargado correctamente")
#             #return redirect('clientes')
#     else:
#         form = ClienteForm()
#     dato = {"form": form}
#     return render(request, template_name, dato)

####################################################################################

# trabajar con modelos (models)
# from .models import Persona
# def cliente(request, template_name='entidad/clientes.html'):
#     cliente_list = Persona.objects.all()
#     dato = {"clientes": cliente_list}
#     return render(request, template_name, dato)

# Obtener un registro por id
# from .models import Localidad
# path('localidad/<int:id_localidad>', views.localidad, name='localidad')
# def localidad(request,id_localidad,template_name='entidad/localidad.html'):
#     localidad_objeto = Localidad.objects.get(id=id_localidad) -> retorna un unico registro
#     dato = {"localidad":localidad_objeto}
#     return render(request, template_name, dato)

def clientes(request, template_name='entidad/clientes.html'):
    cliente_list = Cliente.objects.all()
    dato = {"clientes": cliente_list}
    return render(request, template_name, dato)  ## render(request, ruaDondeSeEncuentraElArchivoHTML, Diccionario)

def cliente(request, DNI_cliente, template_name='entidad/cliente.html'):
    cliente_objeto = Cliente.objects.get(DNI=DNI_cliente)
    dato = {"cliente":cliente_objeto}
    return render(request, template_name, dato)

# def nuevo_cliente(request, template_name='entidad/cliente_form.html'):
#     if request.method == 'POST':
#         form = ClienteForm(request.POST)
#         if form.is_valid():
#             Cliente.objects.create(
#                 DNI = form.cleaned_data['DNI'],
#                 nombre = form.cleaned_data['nombre'],
#                 apellido = form.cleaned_data['apellido'],
#                 direccion = form.cleaned_data['direccion']
#             )
#             return redirect('clientes')
#     else:
#         form = ClienteForm()
#     dato = {"form": form}
#     return render(request, template_name, dato)

def nuevo_cliente(request, template_name='entidad/cliente_form.html'):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('clientes')
    else:
        form = ClienteForm()
    dato = {'form': form}
    return render(request, template_name, dato)


def animales(request, template_name='entidad/animales.html'):
    animal_list = Animal.objects.all()
    dato = {"animales": animal_list}
    return render(request, template_name, dato)

def animalito(request, id_animal, template_name='entidad/animal.html'):
    animal_objeto = Animal.objects.get(id=id_animal)
    dato = {"animal": animal_objeto}
    return render(request, template_name, dato)

# def nuevo_animal(request, template_name='entidad/animal_form.html'):
#     if request.method == 'POST':
#         form = animalForm(request.POST)
#         if form.is_valid():
#             Animal.objects.create(
#                 nombre = form.cleaned_data['nombre'],
#                 raza = form.cleaned_data['raza'],
#                 categoria = form.cleaned_data['categoria'],
#                 duenio = form.cleaned_data['duenio']
#             )
#             return redirect('animales')
#     else:
#         form = animalForm()
#     dato = {"form": form}
#     return render(request, template_name, dato)
def nuevo_animal(request, template_name='entidad/animal_form.html'):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('animales')
    else:
        form = AnimalForm()
    dato = {'form': form}
    return render(request, template_name, dato)

def modificar_cliente(request, pk, template_name='entidad/cliente_form.html'):
    cliente = Cliente.objects.get(id=pk)
    form = ClienteForm(request.POST or None, instance=cliente)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=True)
            return redirect('clientes')
    dato = {'form': form}
    return render(request, template_name, dato)

def modificar_animal(request, pk, template_name='entidad/animal_form.html'):
    animal = Animal.objects.get(id=pk)
    form = AnimalForm(request.POST or None, instance=animal)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=True)
            return redirect('animales')
    dato = {'form': form}
    return render(request, template_name, dato)

def eliminar_cliente(request, pk, template_name='entidad/confirmar_eliminacion.html'):
    cliente_e = Cliente.objects.get(id=pk)
    if request.method == 'POST':
        cliente_e.delete()
        return redirect('clientes')
    dato = {"objeto": "el cliente",
            "dato": cliente_e.nombre + ", " + cliente_e.apellido}
    return render(request, template_name, dato)

def eliminar_animal(request, pk, template_name='entidad/confirmar_eliminacion.html'):
    animal = Animal.objects.get(id=pk)
    if request.method == 'POST':
        animal.delete()
        return redirect('animales')
    dato = {"objeto": "el animal",
            "dato": animal.nombre + ", " + animal.raza }
    return render(request, template_name, dato)
