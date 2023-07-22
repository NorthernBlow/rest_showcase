from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from imagekit.models import ImageSpecField
from imagekit.processors import SmartResize





class User(models.Model):
   name = models.CharField(max_length=255, null=False)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)


   def __str__(self):
       return self.name




## категории товаров
class Category(MPTTModel):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    photo = models.ImageField(upload_to='content/images/%Y%m%d/', blank=True)
    parent = TreeForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)


    class MPTTMeta:
        order_insertion_by = ['name']


    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'

    #вместо QuerySet названия объекта используем метод для строкового представления объекта
    def __str__(self):
        return self.name





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
    image = models.ImageField(upload_to='content/album_images/%Y%m%d/', blank=True, null=True)
    image_small = ImageSpecField(source='image', processors=[SmartResize(300, 300)],
                                 format='JPG',
                                 options={'quality': 90})
    image_medium = ImageSpecField(source='image', processors=[SmartResize(600, 600)],
                                  format='JPG',
                                  options={'quality': 97})
    price = models.DecimalField(max_digits=10, decimal_places=2)


## называем по-человечески модель.
    class Meta:
        verbose_name_plural = 'Продукты'
        verbose_name = 'Продукт'

    def __str__(self):
        return self.product_name



class Cart(models.Model):
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    total = models.DecimalField(max_digits=50, decimal_places=2, default=1)
    quantity = models.IntegerField(null=False)
    item = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)



    def calculate_total_price(self):
        total_price = sum(product.price for product in self.item.all())
        return total_price




