#Добавлено-1 - загрузка динамического контента из json-файла
#Добавлено-2 - загрузка из БД вместо json-файла

from datetime import datetime
from django.shortcuts import render
from products.models import Product, ProductCategory

# MODULE_DIR = os.path.dirname(__file__)

# Create your views here.

def index(request):
	context = {
	'title': 'Geekshop',
	'date': datetime.now(),
	}
	return render(request, 'products/index.html', context)

# def products(request):
# 	file_path = os.path.join(MODULE_DIR, 'fixtures/goods.json')
# 	context = {
# 	'title': 'Geekshop - Каталог',
# 	'products': json.load(open(file_path, encoding='utf-8'))
# 	}
# 	return render(request, 'products/products.html', context)

def products(request):
	context = {
		'title': 'Geekshop - Каталог',
		'products': Product.objects.all(),
		'categories': ProductCategory.objects.all(),
	}
	return render(request, 'products/products.html', context)