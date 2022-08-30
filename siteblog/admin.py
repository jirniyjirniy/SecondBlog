from django.contrib import admin
from django import forms

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

from siteblog.models import Post, Category, Tag, DayPost


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Post
        fields = '__all__'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)
    }
    form = PostAdminForm
    save_on_top = True
    list_display = ('id', 'title', 'slug', 'category', 'created_at', 'get_photo')
    list_display_links = ('id', 'title',)
    search_fields = ('title',)
    list_filter = ('category', 'tags')
    readonly_fields = ('view', 'created_at', 'get_photo',)
    fields = ('title', 'slug', 'category', 'tags', 'content', 'photo', 'author', 'get_photo', 'view', 'created_at',)


    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(mark_safe(f'<img src={obj.photo.url} width="50" height="50"'))
        return '-'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)
    }
    list_display = ('id', 'title', 'slug',)
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    save_on_top = True

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)
    }
    list_display = ('id', 'title', 'slug',)
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    save_on_top = True


@admin.register(DayPost)
class DayPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)
    }
    form = PostAdminForm
    save_on_top = True
    save_as = True
    list_display = ('id', 'title', 'slug', 'category', 'created_at', 'get_photo')
    list_display_links = ('id', 'title',)
    search_fields = ('title',)
    list_filter = ('category', 'tags')
    readonly_fields = ('view', 'created_at', 'get_photo',)
    fields = ('title', 'slug', 'category', 'tags', 'content', 'photo', 'author', 'get_photo', 'view', 'created_at',)


    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(mark_safe(f'<img src={obj.photo.url} width="50" height="50"'))
        return '-'
