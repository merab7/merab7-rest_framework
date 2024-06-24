from algoliasearch_django import AlgoliaIndex
from .models import Products
from algoliasearch_django.decorators import register




@register(Products)
class ProductIndex(AlgoliaIndex):
    should_index = 'is_public'
    fields = [
        'title',
        'content',
        'price',
        'user',
        'public'
    ]

    tags = 'get_tags_list'