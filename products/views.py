from itertools import product
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from .serializers import ReviewSerializer
from .models import Product
from .models import Review


@api_view(['GET', 'POST'])
def products_list(request):

  if request.method == 'GET':
    products = Product.objects.all()                     
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


  elif request.method == 'POST':   
    serializer = ProductSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

    
@api_view(['GET', 'PUT', 'DELETE'])
def products_detail(request, pk): 
  product = get_object_or_404(Product, pk=pk) 
  if request.method == 'GET': 
    serializer = ProductSerializer(product)
    return Response(serializer.data) 
  elif request.method == 'PUT':
    serializer = ProductSerializer(product, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)
  elif request.method == 'DELETE':
      product.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def reviews_list(request, fk=''):

  if request.method == 'GET':
    reviews = Review.objects.all()                     
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)  

  elif request.method == 'POST':
    found_product = Product.objects.get(id=fk)   
    serializer = ReviewSerializer(data = request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save(product = found_product)
    return Response(serializer.data, status=status.HTTP_201_CREATED)  

@api_view(['GET', 'PUT', 'DELETE'])
def reviews_detail(request, pk): 
  review = get_object_or_404(Review, pk=pk) 
  if request.method == 'GET': 
    serializer = ReviewSerializer(review)
    return Response(serializer.data) 
  elif request.method == 'PUT':
    serializer = ReviewSerializer(review, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)
  elif request.method == 'DELETE':
      review.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def all_reviews_by_product(request,fk):
    reviews = Review.objects.filter(product_id = fk)                     
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)  
