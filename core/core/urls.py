from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from northern_label.views import CategoryAPIView, ProductAPIView


#router = DefaultRouter()
#router.register()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/categorylist/', CategoryAPIView.as_view()),
    path('api/v1/productlist/', ProductAPIView.as_view())
]


