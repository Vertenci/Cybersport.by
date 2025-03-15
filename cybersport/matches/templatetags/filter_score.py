from django import template

register = template.Library()

@register.filter
def format_score(value):
    return value.replace(':', ' : ')
