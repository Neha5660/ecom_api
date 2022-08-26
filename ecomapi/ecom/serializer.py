from rest_framework import serializers
from .models import Categories,Cloth,Product

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Categories
        fields=['id','title']

class ClothSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cloth
        fields=['id','title','category','size','price','status','date_created','stock']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['id','product_tag','name','category','price','status','date_created','stock']
