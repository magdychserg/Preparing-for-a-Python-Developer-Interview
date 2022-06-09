from django.contrib import admin
from .models import Product, Category, DescriptionProduct

# Register your models here.
admin.site.register(Product)
admin.site.register(DescriptionProduct)
admin.site.register(Category)
