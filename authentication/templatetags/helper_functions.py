from django import template

register = template.Library()


@register.filter(name='is_active_item')
def is_active_item(value, param):
    paths = {
        'home': '/',
        'about': '/about/',
        'services': '/services/',
        'portfolio': '/portfolio/',
        'team': '/our-team/',
        'blog': '/blogs/',
        'contact': '/contact/',
        'my_account': '/auth/my-account/',
        'account_blogs': '/auth/blogs/',
    }

    for item in paths:
        if value == paths[item] and param == item:
            return 'active'

    return ''