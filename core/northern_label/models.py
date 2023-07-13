from enum import unique
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey



## категории товаров
class Category(MPTTModel):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    photo = models.ImageField(upload_to='content/images/%Y%m%d/', blank=True)
    parent = TreeForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)


    class MPTTMeta:
        order_insertion_by = ['name']


## objects - менеджер, который занимается обработкой данных в модели. в данном случае забираем из нее все поля.
    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'

    #вместо QuerySet названия объекта используем метод для строкового представления объекта
    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('northern_label:category_list', args=[self.slug])



class Brand(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='brands', null=True, blank=True)


    class Meta:
        verbose_name_plural = 'Бренды'
        verbose_name = 'Бренд'


    def __str__(self):
        return self.name



## продавцы
class Product(models.Model):
    product_name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    by_brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='subcategories', null=True, blank=True)
    by_category = TreeForeignKey("Category", on_delete=models.SET_NULL, related_name='categories', null=True, blank=True)
    image = models.ImageField(upload_to='content/album_images/%Y%m%d/', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)


## называем по-человечески модель.
    class Meta:
        verbose_name_plural = 'Продукты'
        verbose_name = 'Продукт'

    def __str__(self):
        return self.product_name
