from django import template
from siteblog.models import Category, DayPost


register = template.Library()

@register.inclusion_tag('blog/menu_tpl.html')
def show_menu(menu_class='menu'):
    categories = Category.objects.all()
    return {'categories': categories, 'menu_class': menu_class}


@register.inclusion_tag('blog/day_post.html')
def get_post_day(count=1):
    post = DayPost.objects.order_by('-id')[:count]
    return {'post': post}