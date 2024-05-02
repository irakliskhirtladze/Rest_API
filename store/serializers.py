from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from store.models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['name', 'price', 'stock', 'category']


class ProductListSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ['name', 'price']


class ProductUpdateSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ['stock']
