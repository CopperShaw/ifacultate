from django import template

register = template.Library()


@register.filter
def add_half(value):
    return value + 0.5
