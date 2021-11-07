from django.urls import path
from products.views import products

app_name = 'products'

urlpatterns = [
    path('', products, name='index'), # без фильтра
    path('<int:category_id>/', products, name='category') # c фильтром по категории товара
]