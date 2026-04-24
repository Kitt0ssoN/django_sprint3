from django.contrib import admin
from .models import Category, Location, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'is_published',
        'created_at'
    )
    list_editable = ('is_published',)
    search_fields = ('title', 'slug')


class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'is_published',
        'created_at'
    )
    list_editable = ('is_published',)
    search_fields = ('name',)


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'is_published',
        'pub_date',
        'category',
        'location',
        'created_at'
    )
    list_editable = ('is_published', 'category', 'location')
    search_fields = ('title',)


admin.site.empty_value_display = 'Не задано'

admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Post, PostAdmin)
