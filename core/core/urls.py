from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from northern_label.views import  CartViewSet, CategoryAPIView, ProductViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView



router = DefaultRouter()
router.register(r"product", ProductViewSet)
router.register(r"cart", CartViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/v1/categorylist/', CategoryAPIView.as_view()),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/docs', SpectacularSwaggerView.as_view(url_name='schema'))
]


