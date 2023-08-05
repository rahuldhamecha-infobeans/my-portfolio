from django import template
from django.utils.http import urlsafe_base64_encode
import re


register = template.Library()


@register.filter(name='get_sub_text')
def get_sub_text(value,param=50):
    return value[:param]+'....'

@register.filter(name='replace_special_charcter')
def replace_special_charcter(value,param = ''):
    string = param.join(e for e in value if e.isalnum())
    return string.lower()

def url_encode_safe_value(value):
    return urlsafe_base64_encode(value)

@register.filter(name='slugify')
def slugify(value):
  value = value.lower().strip()
  value = re.sub(r'[^\w\s-]', '', value)
  value = re.sub(r'[\s_-]+', '-', value)
  value = re.sub(r'^-+|-+$', '', value)
  return value

@register.filter(name='blog_length')
def blog_length(value):
    blog_len = value.blog_set.filter(status=True)
    return len(blog_len)