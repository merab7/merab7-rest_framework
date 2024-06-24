from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Q
import random

User = get_user_model()



TAGS_MODEL_VALUES = ['electronics', 'cars', 'cameras', 'boats']


class ProductQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter()
    
    def search(self, query, user=None):
        lookup =Q(title__incontains=query) | Q(content__icontains=query)
        qs = self.is_public().filter(lookup)
        if user is not None:
            qs2 = self.filter(user=user).filter(lookup)
            qs = (qs | qs2).distinct()
        return qs    



class ProductMenager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return ProductQuerySet(self.model, using=self._db)
    
    def search(self, query, user=None):
        return self.get_queryset().search(query, user=user)


class Products(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price  = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)
    public = models.BooleanField(default=True)
    objects = ProductMenager()


    def is_public(self):
        return self.public
    
    def get_tags_list(self):
        return [random.choice(TAGS_MODEL_VALUES)]
  
    @property
    def sale_price(self):
        return "%.2f"%(float(self.price)*0.8)
    
    def get_discount(self):
        return "123"
    
    def __str__(self) -> str:
        return f"{self.title}"
    