import re

from django import template
register = template.Library()


@register.filter        
def truncatechars(value, limit):
    try:
        limit = int(limit)
    except ValueError: # invalid literal for int()
        return value # Fail silently. 
    if len(value) <= limit:
        truncated_value = value
    else:
        truncated_value = value[0:limit-3]
    return truncated_value
    
@register.filter
def uppercase(value):
	return value.upper()