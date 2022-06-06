
from django.urls import path

from .views import *

urlpatterns = [
    path('', ProductListView.as_view(), name='product'),
    path('descript/', DescriptionListView.as_view(), name='descript'),
    path('category/', CategoryListView.as_view(), name='category'),


]