from django.http import JsonResponse
from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from apps.products.views import PriceVariationViewSet, ProductViewSet
from apps.users.views import RegisterViewSet


def health_check(request):
    return JsonResponse({"status": "ok"})


router = routers.DefaultRouter()

router.register(r"register", RegisterViewSet)
router.register(r'products', ProductViewSet, basename='products')
router.register(r'price-variations', PriceVariationViewSet,
                basename='price-variations')


urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('healthcheck/', health_check, name='health_check'),

]
