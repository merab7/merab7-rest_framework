from rest_framework import viewsets, mixins
from .models import Products
from .serializers import ProductsSerializer



class ProductViewSet(viewsets.ModelViewSet):
    
    """
    get --> list --> Queryset
    get --> retrieve --> Product Instance Detail View
    post --> create --> New Instance
    put --> Update
    patch --> Partial Update
    delete --> destroy
     """
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    lookup_field = 'pk' #default
   


class ProductGenericViewSet(
    viewsets.GenericViewSet, 
    mixins.ListModelMixin, 
    mixins.RetrieveModelMixin):
    """
    get --> list --> Queryset
    get --> retrieve --> Product Instance Detail View
     """
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    lookup_field = 'pk' #default
