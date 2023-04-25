from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse


## категории товаров
class Artists(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    photo = models.ImageField(upload_to='content/images/%Y%m%d/', blank=True)
    is_published = models.BooleanField(default=True)
    description = models.CharField(max_length=255, blank=True)


## objects - менеджер, который занимается обработкой данных в модели. в данном случае забираем из нее все поля.
    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    class Meta:
        verbose_name_plural = 'Музыкальные исполнители'
        verbose_name = 'Музыкальный исполнитель'

    #вместо QuerySet названия объекта используем метод для строкового представления объекта
    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('northern_label:category_list', args=[self.slug])



## продавцы
class Release(models.Model):
    release_name = models.CharField(max_length=255, db_index=True)
    title = models.CharField(max_length=255, default='Релиз', blank=False)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(max_length=1000, default='', blank='false')
    category_by_artists = models.ForeignKey(Artists, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='content/album_images/%Y%m%d/', blank=True)

## называем по-человечески модель.
    class Meta:
        verbose_name_plural = 'Релизы'
        verbose_name = 'Релиз'


    def get_absolute_url(self):
        return reverse('northern_label:category_list', args=[self.slug])


    def register(self):
        self.save()

    @staticmethod
    def get_all_releases():
        return Release.objects.all()

    @staticmethod
    def get_releases_by_category(category_id):
        if category_id:
            return Release.objects.filter(category=category_id)
        else:
            return Release.get_all_albums()

    def isExists(self):
        if Release.objects.filter(release_name=self.release_name):
            return True
        return False

    def __str__(self):
        return self.title

