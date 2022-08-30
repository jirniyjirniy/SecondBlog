from django import template
from siteblog.models import Post, Tag

register = template.Library()

@register.inclusion_tag('blog/popular_posts.html')
def get_popular(count=4):
    posts = Post.objects.order_by('-view')[:count]
    return {'posts': posts}


@register.inclusion_tag('blog/tags.html')
def get_tags():
    tags = Tag.objects.all()
    return {'tags': tags}