from django import template
import os

register = template.Library()

# Filtro para obtener un valor de un diccionario por clave
@register.filter
def get_item(dictionary, key):
    """Devuelve el valor de un diccionario dado una clave."""
    return dictionary.get(key, None)

#Filtro para obtener el nombre base de un archivo a partir de su ruta
@register.filter
def basename(value):
    """Devuelve el nombre base de un archivo a partir de su ruta."""
    return os.path.basename(value)
