from django.contrib import admin
from products.models import ProductCategory, Product

admin.site.register(ProductCategory)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # отображение нескольких параметров в строке в products
    list_display = ('name', 'quantity', 'price')
    # изменение порядка полей в форме добавления, значения во вложенном кортеже будут объединены в одну строку
    fields = ('name', 'image', 'description', ('price', 'quantity'), 'category')
    # поля только для чтения
    readonly_fields = ('description',)
    # сортировка в алфавитном порядке
    ordering = ('name',)
    # поиск по названию
    search_fields = ('name',)