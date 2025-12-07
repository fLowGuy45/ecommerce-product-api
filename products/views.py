from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, filters
from .models import Product, Category
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name','description','category__name']
    ordering_fields = ['price_cents','created_at']
