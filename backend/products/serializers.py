from rest_framework import serializers
from  .validators import validate_title
from .models import Products
from rest_framework.reverse import reverse 
from api.serializers import UserPublicSerializer


class ProductsSerializer(serializers.ModelSerializer):
    
    user = UserPublicSerializer(read_only=True)

    my_discount = serializers.SerializerMethodField(read_only = 99.99)

    #detail url 
    url = serializers.SerializerMethodField(read_only = True)
    
    #edit url 
    edit_url = serializers.SerializerMethodField(read_only = True)

    title = serializers.CharField(validators=[validate_title])

    # user = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Products
        fields = [
            'user',
            'edit_url',
            'url',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]



    def get_url(self, obj):

        request = self.context.get('request')

        if request is None:
            return None
        
        return reverse("product-detail", kwargs={"pk":obj.pk}, request=request)


    # def get_user(self, obj):
        
    #     request = self.context.get('request')
        
    #     if request is None:
    #         return None

        
    #     if obj.user == request.user:
    #         return obj.user.username

        

    def get_edit_url(self, obj):

        request = self.context.get('request')

        if request is None:
            return None
        
        return reverse("product-edit", kwargs={"pk":obj.pk}, request=request)


    def get_my_discount(self, obj):
        try:
           return obj.get_discount()
        except:
            return None    

 