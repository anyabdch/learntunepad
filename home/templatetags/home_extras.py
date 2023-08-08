from django import template

register = template.Library()

@register.filter(name="index")
def index(lst, idx):
    return lst[idx]

@register.filter(name="children")
def children(par):
    return par.get_children()

@register.filter(name="values")
def values(qs):
    return qs.values()

@register.filter(name="isproject")
def proj(id):
    return id.isnumeric()