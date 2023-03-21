from rest_framework import serializers

from .models import Product, Stock, StockProduct

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'title', 'description']

    def create(self, validated_data):
        stock = super().create(validated_data)
        return stock

    def update(self, instance, validated_data):
        stock = super().update(instance, validated_data)
        return stock


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['id', 'address', 'positions']

    def create(self, validated_data):
        positions = validated_data.pop('positions')

        stock = super().create(validated_data)

        for p in positions:
            StockProduct.objects.create(stock=stock, **p)

        return stock

    def update(self, instance, validated_data):
        positions = validated_data.pop('positions')

        stock = super().update(instance, validated_data)

        for p in positions:
            product = positions['product']
            print(product)
            StockProduct.objects.update_or_create(stock=stock, product=product, defaults={
                                                                'quantity': p['quantity'],
                                                                'price': p['price']})

        return stock
