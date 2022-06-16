from django import template
from post.models import Category

register = template.Library()

@register.inclusion_tag('post/categories_tpl.html')
def category():
    categories = Category.objects.all()
    return {'categories': categories}
