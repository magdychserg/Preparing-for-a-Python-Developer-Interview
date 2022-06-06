from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render
from django.views.generic import ListView
from .models import Product,DescriptionProduct,Category

class UserListView(ListView):
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        return context


class ProductListView(UserListView):
    model = Product
    queryset = Product.on_site.all()
    template_name = 'product/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({

            'site': get_current_site(request=self.request)
        })
        return context

class CategoryListView(UserListView):
    model = Category
    # queryset = Category.objects.prefetch_related('products').all()
    queryset = Category.on_site.prefetch_related('products').all()
    template_name = 'product/categories.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({

            'site': get_current_site(request=self.request)
        })
        return context


class DescriptionListView(UserListView):
    model = DescriptionProduct
    queryset = DescriptionProduct.objects.select_related('product').all()
    template_name = 'product/description.html'

