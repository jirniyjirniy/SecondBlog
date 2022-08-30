from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')
    author = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True, verbose_name='Опубликовано')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    view = models.IntegerField(default=0, verbose_name='Количество просмотров')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='posts')
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={
            'slug': self.slug,
        })

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Category(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={
            'slug': self.slug,
        })

    class Meta:
        ordering = ['title']
        verbose_name = 'Категория(ю)'
        verbose_name_plural = 'Категории'

class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=150, unique=True, verbose_name='Tag')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag', kwargs={
            'slug': self.slug,
        })

    class Meta:
        ordering = ['title']
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

class DayPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')
    author = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True, verbose_name='Опубликовано')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    view = models.IntegerField(default=0, verbose_name='Количество просмотров')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='post')
    tags = models.ManyToManyField('Tag', blank=True, related_name='post')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('day-post', kwargs={
            'slug': self.slug,
        })

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Пост дня'
        verbose_name_plural = 'Посты дня'