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
    queryset = Product.objects.all()
    template_name = 'product/index.html'


class CategoryListView(UserListView):
    model = Category
    queryset = Category.objects.prefetch_related('products').all()
    # queryset = Book.on_site.prefetch_related('authors').all()
    template_name = 'product/categories.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        return context


class DescriptionListView(UserListView):
    model = DescriptionProduct
    queryset = DescriptionProduct.objects.select_related('product').all()
    template_name = 'product/description.html'
    # extra_context = {
    #     'user': {'name': 'Denis', 'age': '41'}
    # }

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context.update({
    #         'user': {'name': 'Denis', 'age': '41'}
    #     })
    #     return context


# def return_extra():
#     return {'name': 'Denis', 'age': '41'}


# def get_page(request):
#     return render(request, 'index.html', context={
#         'object_list': Author.objects.all(),
#         'user': return_extra()
#     })
#
#
# def get_page_1(request):
#     return render(request, 'index1.html', context={
#         'object_list_1': Author.objects.all(),
#         'user': return_extra()
#     })