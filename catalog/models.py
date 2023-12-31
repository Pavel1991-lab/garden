from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='название')
    description = models.TextField(verbose_name='описание')

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')  # наименование
    description = models.TextField(verbose_name='описание')  # описание
    image = models.ImageField(upload_to='product_images', blank=True, null=True)  # изображение (превью)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена')  # цена за покупку
    created_date = models.DateTimeField(auto_now_add=True)  # дата создания
    last_modified_date = models.DateTimeField(auto_now=True)  # дата последнего изменения


# class Blog(models.Model):
#     title = models.CharField(max_length=100, verbose_name='название')
#     slug = models.CharField(max_length=150, verbose_name='slug', null=True, blank=True)
#     content = models.TextField(verbose_name='содержимое')
#     preview = models.ImageField(upload_to='blog_previews', blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     is_published = models.BooleanField(default=False)
#     views_count = models.IntegerField(default=0)
#
#
#
