from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Category, FilterAdvert, DateAdvert, Advert


@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    list_display = ('name', 'id')
    mptt_level_indent = 20
    prepopulated_fields = {'slug': ('name',)}


@admin.register(FilterAdvert)
class FilterAdvertAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(DateAdvert)
class FilterAdvertAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    

@admin.register(Advert)
class FilterAdvertAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'subject', 
        'user', 
        'category', 
        'filter', 
        'date', 
        'price', 
        'created', 
        'moderation'
    )
    list_display_links = ('subject',)
    list_filter = ('user', 'category', 'filter', 'date', 'price',)
    prepopulated_fields = {'slug': ('user', 'subject')}


 