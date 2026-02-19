from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('products/', views.ProductListView.as_view(), name='product_list'),
    path('category/<int:category_id>/products/', views.CategoryProductsView.as_view(), name='category_products'),
]