from django.http import JsonResponse
from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from apps.products.views import PriceVariationViewSet, ProductViewSet
from apps.users.views import RegisterViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


def health_check(request):
    return JsonResponse({"status": "ok"})


schema_view = get_schema_view(
    openapi.Info(
        title="Your Project API",
        default_version='v1',
        description="Description of your API",
        terms_of_service="https://www.yoursite.com/terms/",
        contact=openapi.Contact(email="contact@yoursite.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

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
    path('swagger<str:format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]
