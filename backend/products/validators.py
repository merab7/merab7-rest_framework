from ctypes import resize
from rest_framework import serializers
from .models import Products
from rest_framework.validators import UniqueValidator

def validate_title(value):
    qs = Products.objects.filter(title__iexact = value)
    if qs.exists():
        raise serializers.ValidationError(f"{value} is already a product name.")
    
    return value 

def validate_title_no_gello(value):
    if "hello" in value.lower():
        raise serializers.ValidationError('hello is not allowed')
    return value


unique_product_title = UniqueValidator(queryset=Products.objects.all())