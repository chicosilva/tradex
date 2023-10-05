from rest_framework import serializers

from .models import PriceVariation, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class PriceVariationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceVariation
        fields = '__all__'


class ProductDetailsSerializer(serializers.ModelSerializer):
    pricevariations = PriceVariationDetailSerializer(many=True)

    class Meta:
        model = Product
        fields = ['name', 'image', 'ean', 'min_price',
                  'max_price', 'pricevariations']


class PriceVariationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceVariation
        fields = '__all__'

    def validate_price(self, value):
        """
        Validate that the price falls within the range specified by min_price and max_price.
        """

        product_id = self.initial_data.get('product')
        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            raise serializers.ValidationError("Invalid product ID.")

        min_price = product.min_price
        max_price = product.max_price

        if not (min_price <= value <= max_price):
            raise serializers.ValidationError(
                "Price must be within the range of min_price and max_price.")

        return value

    def validate(self, data):
        """
        Validate if start_date and end_date period already exists.
        """

        product = data.get('product')

        start_date = data.get('start_date')
        end_date = data.get('end_date')

        if start_date and end_date:
            qs = PriceVariation.objects.filter(
                product=product,
                start_date__lte=end_date,
                end_date__gte=start_date
            )

            if self.instance:
                qs = qs.exclude(pk=self.instance.pk)

            if qs.exists():
                raise serializers.ValidationError(
                    "Price variation for the given period already exists.")

        return data
