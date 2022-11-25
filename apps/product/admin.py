from django.contrib import admin

# Register your models here.
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = (['name'])
    search_fields = (['name'])


class ProductAdmin(admin.ModelAdmin):
    list_display = (['title', 'created', 'modified'])
    search_fields = (['title'])


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
