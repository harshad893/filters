from django import template
register=template.Library()

@register.filter(name='low')
def lower(value):
    return value.lower()

@register.filter(name='replace')
def replace_char(value,arg):
    return value.replace(arg,'b')

@register.filter()
def remove(value,arg):
    return value.replace(arg,'')



#register.filter('low',lower)
#register.filter('rep',replace_char)

