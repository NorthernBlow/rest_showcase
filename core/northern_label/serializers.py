from rest_framework import serializers
from northern_label.models import Category, Brand, Product




class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"



class CategorySerializer(serializers.ModelSerializer):
    subcategories = BrandSerializer(many=True, read_only=True)
	
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
