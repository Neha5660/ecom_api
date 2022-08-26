from django.shortcuts import render
from rest_framework import generics

from .models import Categories,Cloth,Product
from .serializer import CategoriesSerializer,ClothSerializer,ProductSerializer

# Create your views here.
class ListCategories(generics.ListCreateAPIView):
    queryset=Categories.objects.all()
    serializer_class = CategoriesSerializer


class DetailCategories(generics.RetrieveUpdateDestroyAPIView):
    queryset=Categories.objects.all()
    serializer_class = CategoriesSerializer


class ListCloth(generics.ListCreateAPIView):
    queryset=Cloth.objects.all()
    serializer_class = ClothSerializer


class DetailCloth(generics.RetrieveUpdateDestroyAPIView):
    queryset=Cloth.objects.all()
    serializer_class = ClothSerializer

class ListProduct(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class = ProductSerializer

class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class = ProductSerializer
    