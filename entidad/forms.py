from django import forms
from django.forms import ModelForm
from .models import Animal, Cliente

# class animalForm(forms.Form):
#     nombre = forms.CharField(label='Nombre/s', max_length=120)
#     raza = forms.CharField(label='Raza', max_length=120)
#     categoria = forms.CharField(label='Categoria', max_length=20)
#     duenio = forms.IntegerField(label='Duenio')
class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

# class ClienteForm(forms.Form):
#     DNI = forms.IntegerField(label='DNI')
#     nombre = forms.CharField(label='Nombre', max_length=120)
#     apellido = forms.CharField(label='Apellido', max_length=120)
#     direccion = forms.CharField(label='Direccion', max_length=20)
    
