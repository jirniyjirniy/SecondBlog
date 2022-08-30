from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import F

from siteblog.models import Category, Post, Tag, DayPost


class Home(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 4
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Classic Blog Design'
        return context


class GetPost(DetailView):
    model = Post
    template_name = 'blog/single.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.view = F('view') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context

class GetDayPost(DetailView):
    model = DayPost
    template_name = 'blog/single_day_post.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.view = F('view') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context


class PostByCategory(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 4
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Posts by category: {Category.objects.get(slug=self.kwargs["slug"])}'
        return context


class PostByTag(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 4
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context =super().get_context_data(**kwargs)
        context['title'] = f'Entries by tag: {Tag.objects.get(slug=self.kwargs["slug"])}'
        return context


class Search(ListView):
    template_name = 'blog/search.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get('s'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = f"s={self.request.GET.get('s')}&"
        return context