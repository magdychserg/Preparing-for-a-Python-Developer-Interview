from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from .models import Product, Category

def product_list(request):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()

    return render(request, 'product\index.html',
                  {'category': category, 'categories': categories,
                   'products': products})


class ProductDeatail(DetailView):
    model = Product
    template_name = 'product\index.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDeatail, self).get_context_data(**kwargs)
        product = self.get_object()
        context['product'] = product
        return context
# class UserListView(ListView):
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         context.update({
#
#         })
#         return context
#
# class ProductListView(UserListView):
#     model = Product
#     queryset = Product.objects.all()
#     template_name = 'index.html'
#
# class CategoryListView(UserListView):
#     model = Category
#     queryset = Category.objects.select_related('product').all()
#
#     template_name = 'category.html'
#
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         # context.update({
#         #     'user': {'name': 'Denis', 'age': '41'},
#         return context