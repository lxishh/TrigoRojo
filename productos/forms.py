from django import forms
from productos.models import Producto, Categoria
import re


class FormularioProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('nombre', 'codigo', 'descripcion', 'precio', 'categoria')
        labels = {
            'nombre': 'Nombre del producto:',
            'codigo': 'Codigo del producto',
            'descripcion': 'Descripción:',
            'precio': 'Precio:',
            'categoria': 'Categoría:',
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')

        # Validación para evitar números en el nombre
        if any(char.isdigit() for char in nombre):
            raise forms.ValidationError('El nombre no puede contener números.')

        # Verifica si ya existe un producto con el mismo nombre, pero que no sea el producto actual
        producto_id = self.instance.id if self.instance.id else None
        if Producto.objects.filter(nombre=nombre).exclude(id=producto_id).exists():
            raise forms.ValidationError(
                'Ya existe un producto con este nombre.')
        return nombre

    def clean_codigo(self):
        codigo = self.cleaned_data.get('codigo')

        # CORRECCIÓN CLAVE: Identificar el producto actual y excluirlo de la búsqueda
        producto_id = self.instance.id if self.instance.pk else None
        
        # Verifica si ya existe un producto con el mismo código, EXCLUYENDO el producto actual
        if Producto.objects.filter(codigo=codigo).exclude(pk=producto_id).exists():
            raise forms.ValidationError(
                'Ya existe un producto con este código.')
        return codigo


class FormularioCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('nombre', 'descripcion',)
        labels = {
            'nombre': 'Nombre de la categoria:',
            'descripcion': 'Descripción:',
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        # Obtiene el ID de la categoría que estamos actualizando
        categoria_id = self.instance.id

        # Validación para evitar números en el nombre
        if any(char.isdigit() for char in nombre):
            raise forms.ValidationError('El nombre no puede contener números.')

        # Verifica si ya existe una categoría con el mismo nombre, pero excluyendo la categoría actual
        if Categoria.objects.filter(nombre=nombre).exclude(id=categoria_id).exists():
            raise forms.ValidationError('Esta categoría ya existe.')

        return nombre