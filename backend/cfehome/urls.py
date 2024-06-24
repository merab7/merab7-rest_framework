from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('search/', include('search.urls')),
    path('product/', include('products.urls')),
    path('v2/', include('cfehome.routers')),
]

