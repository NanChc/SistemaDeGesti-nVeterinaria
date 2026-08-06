from django.db import models

# Create your models here.
class Cliente(models.Model):
    DNI = models.IntegerField("DNI", null=True, blank=True)
    nombre = models.CharField("Nombre", max_length=50)
    apellido = models.CharField("Apellido", max_length=20, blank=True)
    direccion = models.CharField("Direccion", max_length=50, blank=True)
    
    def __str__(self):
        return self.nombre

class Animal(models.Model):
    nombre = models.CharField("Nombre", max_length=50)
    raza = models.CharField("Raza", max_length=50)
    categoria = models.CharField("Categoria", max_length=20)
    duenio = models.ForeignKey(Cliente, on_delete=models.PROTECT, null=True, blank=True)




# en la terminal correr -> python manage.py makemigrations
#despues --> python manage.py migrate

# --> python manage.py shell
# --> from entidad.models import Localidad
# --> lujan = Localidad(nombre="lujan", cp="b6700", provincia="Buenos Aires")
# --> lijan.save()
# --> lijan.id

# O OTRA FORMA MAS RAPIDA
# lo crea mas rapido
#--> clorinda = Localidad.objects.create(nombre="clorinda", cp="p3610", provincia="Formosa")