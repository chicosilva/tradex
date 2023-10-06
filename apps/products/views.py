from rest_framework import status, viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from apps.products.filters import ProductFilter
from apps.products.models import PriceVariation, Product
from apps.products.serializers import (PriceVariationSerializer,
                                       ProductDetailsSerializer,
                                       ProductSerializer)
from apps.shared.service import SharedService


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    serializer_class_detail = ProductDetailsSerializer
    permission_classes = [IsAdminUser]
    filterset_class = ProductFilter

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        serializer = self.serializer_class_detail(instance, context={"request": request})
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        SharedService().set_canceled(instance=self.get_object(),
                                     user=request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)


class PriceVariationViewSet(viewsets.ModelViewSet):
    queryset = PriceVariation.objects.all()
    serializer_class = PriceVariationSerializer
    permission_classes = [IsAdminUser]

    def destroy(self, request, *args, **kwargs):
        SharedService().set_canceled(instance=self.get_object(),
                                     user=request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)
