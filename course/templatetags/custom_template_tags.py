from django import template
from course.models import Category
register = template.Library()


@register.simple_tag
def load_categorys():
    return Category.objects.all()
