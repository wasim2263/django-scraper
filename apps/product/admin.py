from django.contrib import admin

# Register your models here.
from .models import Category, Product


class BrandAdmin(admin.ModelAdmin):
    list_display = (['name'])
    search_fields = (['name'])


class CategoryAdmin(admin.ModelAdmin):
    list_display = (['name'])
    search_fields = (['name'])


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product)
