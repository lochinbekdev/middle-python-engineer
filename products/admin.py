from django.contrib import admin
from .models import Products


class ProductModel(admin.ModelAdmin):
    list_display=('name','price','stock')


admin.site.register(Products,ProductModel)