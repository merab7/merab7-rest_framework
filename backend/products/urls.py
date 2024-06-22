from django.urls import path
from .views import ProductDetailAPIview, ProductListCreateAPIView, ProductDeleteAPIview,  ProductUpdateAPIview
urlpatterns = [
    path('detail/<int:pk>/', ProductDetailAPIview.as_view()),
    path('delete/<int:pk>/', ProductDeleteAPIview.as_view()),
    path('update/<int:pk>/', ProductUpdateAPIview.as_view()),
    path('create/', ProductListCreateAPIView.as_view()),
    
]