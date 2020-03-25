import re
from django.template.defaultfilters import slugify


def unique_slugify(instance, title):

    slug = slugify(title)
    model_class = instance.__class__

    num = 1
    temp = slug
    while model_class._default_manager.filter(slug=slug).exists():
        slug = f'{slug}-{num}'  
        if(slug[-1].isdigit() and model_class._default_manager.filter(slug=slug).exists()):
            slug=temp
        num+=1

    return slug