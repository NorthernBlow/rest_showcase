from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination
from northern_label.models import Category, Brand, Product
from PIL import Image


class CategoryPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 30



class BrandSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Brand
        fields = ['name', 'slug']



class CategorySerializer(serializers.ModelSerializer):
    brands = BrandSerializer(many=True, read_only=True)


    class Meta:
        model = Category
        fields = ['name', 'slug', 'photo', 'brands']



class ProductSerializer(serializers.ModelSerializer):
    by_category = CategorySerializer()
    image = serializers.ImageField(read_only=True)
    image_small = serializers.ImageField(read_only=True)
    image_medium = serializers.ImageField(read_only=True)


    class Meta:
        model = Product
        fields = ['by_category', 'product_name', 'slug', 'image', \
                'image_small', 'image_medium', 'price']


