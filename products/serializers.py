from rest_framework import serializers
from .models import Product
from .models import Review

class ProductSerializer(serializers.ModelSerializer):
  class Meta: 
    model = Product
    fields = ['id', 'title', 'description', 'price', 'inventory_quantity', 'url']

class ReviewSerializer(serializers.ModelSerializer):
  class Meta: 
    model = Review
    fields = ['id', 'review', 'date_added', 'product']