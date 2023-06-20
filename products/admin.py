from django.contrib import admin
from .models import Products
from .models import Offer


class ProductModel(admin.ModelAdmin):
    list_display=('name','price','stock')


admin.site.register(Products,ProductModel)


class OfferModel(admin.ModelAdmin):
    list_display=('code','discount')


admin.site.register(Offer,OfferModel)