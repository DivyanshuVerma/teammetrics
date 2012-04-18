from django import template

register = template.Library()

def caps(value):
    return value.capitalize()
    
register.filter('caps', caps)
