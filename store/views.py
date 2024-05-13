from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import RetrieveAPIView, CreateAPIView, UpdateAPIView, ListAPIView, DestroyAPIView
from rest_framework.response import Response

from store.models import Product

from store.serializers import ProductSerializer, ProductListSerializer, ProductUpdateSerializer


def start_page(request):
    return render(request, 'index.html')


class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = 'pk'


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductUpdateView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductUpdateSerializer
    lookup_url_kwarg = 'pk'


class ProductDeleteView(DestroyAPIView):
    queryset = Product.objects.all()
    lookup_url_kwarg = 'pk'
