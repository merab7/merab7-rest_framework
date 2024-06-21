from django.urls import path
from .views import ProductDetailAPIview, ProductListCreateAPIView, product_alt_view

urlpatterns = [
    path('<int:pk>/', ProductDetailAPIview.as_view()),
    path('create/', ProductListCreateAPIView.as_view()),
    
]