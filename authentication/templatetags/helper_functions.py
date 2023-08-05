import datetime

from django import template

register = template.Library()


@register.filter(name='is_active_item')
def is_active_item(value, param):
    paths = {
        'home': ['/'],
        'about': ['/about/'],
        'services': ['/services/'],
        'portfolio': ['/portfolio/'],
        'team': ['/our-team/'],
        'blog': ['/blogs/'],
        'contact': ['/contact/'],
        'my_account': ['/auth/my-account/'],
        'account_blogs': ['/auth/blogs/','/auth/blogs/create/'],
    }

    for item in paths:
        if value in paths[item] and param == item:
            return 'active'

    return ''

@register.filter(name='format_date')
def format_date(value):
    return value.strftime('%d-%m-%Y')
