from django.urls import path
from .views import ListCategories,DetailCategories,ListCloth,ListProduct,DetailProduct,DetailCloth

urlpatterns = [
    path('', ListCategories.as_view(), name='categorie'),
    path('<int:pk>/', DetailCategories.as_view(), name='singlecategorie'),
    path('cloth/', ListCloth.as_view(), name='cloth'),
    path('cloth/<int:pk>/', DetailCloth.as_view(), name='singlecloth'),
    path('product/', ListProduct.as_view(), name='product'),
    path('product/<int:pk>/', DetailProduct.as_view(), name='singleproduct'),
]
