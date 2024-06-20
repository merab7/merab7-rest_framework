from rest_framework import serializers
from .models import Products

class ProductsSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only = 99.99)
    class Meta:
        model = Products
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]
    def get_my_discount(self, obj):
        try:
           return obj.get_discount()
        except:
            return None    

 