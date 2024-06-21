from rest_framework import generics
from .models import Products
from .serializers import ProductsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404



class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


    def perform_create(self, serializer):
        return super().perform_create(serializer)


class ProductDetailAPIview(generics.RetrieveAPIView):
    queryset =  Products.objects.all()
    serializer_class  = ProductsSerializer
    # LOOKUP_FIELD = 'PK'


# class ProductListAPIview(generics.ListAPIView):
#     queryset =  Products.objects.all()
#     serializer_class  = ProductsSerializer
#     # LOOKUP_FIELD = 'PK'   
# 
# 
#  

# functiion based view wher is implemanted creation and retrive
@api_view(["GET", "POST"])
def product_alt_view(request, pk=None, *args, **kwargs):
    method  = request.method

    if method == "GET":
       
       if pk is not None:
           obj = get_object_or_404(Products, pk=pk)
           data = ProductsSerializer(obj).data
           return Response(data)
       
       qs = Products.objects.all()
       data = ProductsSerializer(qs, many=True).data
       return Response(data)
    
    if method == "POST":
        serilizer = ProductsSerializer(request.data)
        if serilizer.is_valid(raise_exception=True):

             return Response(serilizer.data)
        return Response({"invalid:" "not good data"}, status=400)
