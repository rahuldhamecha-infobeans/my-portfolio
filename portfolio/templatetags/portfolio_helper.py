from django import template
from django.conf import settings

register = template.Library()


@register.filter(name='get_sub_text')
def get_sub_text(value,param=50):
    return value[:param]+'....'

@register.filter(name='replace_special_charcter')
def replace_special_charcter(value,param = ''):
    string = param.join(e for e in value if e.isalnum())
    return string.lower()